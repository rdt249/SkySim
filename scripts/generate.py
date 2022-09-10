# Stephen Lawrence 2022

import sys,os
import itertools

LIB_NAME = 'MAINLIB_TESTING' # dev use only -- replaced by command line argument
CELL_NAME = 'SL_inv_1x' # dev use only -- replaced by command line argument

# refer to models directory: /home/PDKs/Skywater/V1.10.500/MODELS/SPECTRE/c9fh-3r/Models/
# names of models and pin numbers to connect current source
MODELS = {
    'nshort':[0,3],
    'pshort':[3,0]
}

# naming conventions for important signals
VDD_ALIAS = ['vdd']
VSS_ALIAS = ['vss']
INPUT_ALIAS = ['in','in0','in1']
# todo: add analog inputs and clocks

# global voltage levels
VDD = 1.2
VSS = 0
INPUT_HIGH = 1.2
INPUT_LOW = 0

def read_netlist(cell_name): # read the netlist file, find devices and nets
    file_name = os.path.expanduser(f'~/simulation/{cell_name}/spectre/schematic/netlist/input.scs')
    netlist = open(file_name,'r').read()
    netlist = netlist.replace('\\\n','').split('\n') # undo line breaks
    devices = []
    nets = []
    for i,line in enumerate(netlist):
        if line.startswith('//'): continue # skip comments
        if len(line.split('(')) > 1: # this line is a device
            name = line.split('(')[0]
            pins = line.split('(')[1].split(')')[0].split(' ')
            nets += pins
            model = line.split(')')[1].split()[0]
            params = []
            for param in line.split(model)[1].split(' '): 
                if param != '': params.append(param)
            target = model in MODELS.keys()
            device = {'name':name,'pins':pins,'model':model,'params':params,'line':i,'target':target}
            devices.append(device)
    nets = list(set(nets))
    return netlist,devices,list(set(nets))

def get_stimuli(devices,nets): # generate stimuli (list of lists of strings) based on devices and nets
    targets = []
    for device in devices:
        if device['target']: targets.append(device)
    biases = sum([net in INPUT_ALIAS for net in nets])
    stimuli = []
    test = 0
    for bias in itertools.product([False,True],repeat=biases):
        for target in targets:
            stimulus = []
            stimulus.append(f'// SkySim test{test}')
            stimulus.append(f'// target device: {target["name"]}')
            i = 0
            for net in nets:
                if net in VDD_ALIAS: stimulus.append(f'VDD ({net} 0) vsource dc={VDD}')
                if net in VSS_ALIAS: stimulus.append(f'VSS ({net} 0) vsource dc={VSS}')
                if net in INPUT_ALIAS:
                    if bias[i]: stimulus.append(f'V{i} ({net} 0) vsource dc={INPUT_HIGH}')
                    else: stimulus.append(f'V{i} ({net} 0) vsource dc={INPUT_LOW}')
                    i += 1
            
            nodes = [target['pins'][n] for n in MODELS[target['model']]]
            settings = 'type=pulse val0=0 val1=200u period=100n width=5p rise=1p fall=5p'
            stimulus.append(f'STRIKE ({nodes[0]} {nodes[1]}) isource ' + settings)
            #stimulus.append(f'CAP ({nodes[0]} {nodes[1]}) capacitor c=0.1n')
            #stimulus.append(f'DIODE ({nodes[1]} {nodes[0]}) pdiode area=6')
            stimulus.append('sim tran stop=100p')
            stimulus.append('')
            stimuli.append(stimulus)
    return stimuli

def format_bash(lib_name,cell_name,tests):
    bash = [
        'MODELS="/home/PDKs/Skywater/V1.10.500/MODELS/SPECTRE/c9fh-3r/Models/"',
        'source env/SW_Run/bashrc.IC'
    ]
    for test in tests:
        dir = f'{lib_name}/{cell_name}/test{test}'
        bash.append(f'spectre data/{dir}/input.scs -I/$MODELS -format psfascii -raw data/{dir}')
        bash.append(f'cp input.log data/{dir}/input.log')
        bash.append('rm -r input.ahdlSimDB input.log')
        bash.append(f'python3 scripts/analyze.py {lib_name} {cell_name} test{test}')
    return '\n'.join(bash)

def write_tests(lib_name,cell_name,netlist,stimuli): # write spectre input files (netlist + stimulus)
    root = f'data/{lib_name}/{cell_name}'
    os.makedirs(root,exist_ok=True)
    open(root + '/netlist.scs','w').write('\n'.join(netlist))
    for i in range(len(stimuli)):
        os.makedirs(root + f'/test{i}',exist_ok=True)
        file_name = root + f'/test{i}/input.scs'
        open(file_name,'w').write('\n'.join(netlist + stimuli[i]))
        file_name = root + f'/test{i}/run.sh'
        open(file_name,'w').write(format_bash(lib_name,cell_name,[i]))
        os.chmod(file_name,0o775)
    file_name = root + '/run_all.sh'
    open(file_name,'w').write(format_bash(lib_name,cell_name,range(len(stimuli))))
    os.chmod(file_name,0o775)

def main(lib_name,cell_name):
    netlist,devices,nets = read_netlist(cell_name)
    stimuli = get_stimuli(devices,nets)
    write_tests(lib_name,cell_name,netlist,stimuli)

if __name__ == '__main__':
    if len(sys.argv) > 1: LIB_NAME = sys.argv[1]
    if len(sys.argv) > 2: CELL_NAME = sys.argv[2]
    main(LIB_NAME,CELL_NAME)