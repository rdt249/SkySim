# Stephen Lawrence 2022

import sys,os
import itertools
import pandas as pd

CELL_PATH = 'MAINLIB_TESTING/SL_inv_1x' # dev use only -- replaced by command line argument

# refer to models directory: /home/PDKs/Skywater/V1.10.500/MODELS/SPECTRE/c9fh-3r/Models/
# names of models, along with the pins where we should connect a fault injector to simulate radiation
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

def read_netlist(cell_path): # read the netlist file, find devices and nets
    cell_name = cell_path.split('/')[1] # get the cell name
    file_name = os.path.expanduser(f'~/simulation/{cell_name}/spectre/schematic/netlist/input.scs') # get path
    netlist = open(file_name,'r').read() # open the netlist file
    netlist = netlist.replace('\\\n','').split('\n') # undo line breaks
    devices = []
    nets = []
    for i,line in enumerate(netlist): # for every line in the netlist file
        if line.startswith('//'): continue # skip comments
        if len(line.split('(')) > 1: # this line is a device
            name = line.split('(')[0] # get device identifier
            pins = line.split('(')[1].split(')')[0].split(' ') # get device pins
            nets += pins # add pins to netlist
            model = line.split(')')[1].split()[0] # get device model name
            params = []
            for param in line.split(model)[1].split(' '):  # get each parameter in device
                if param != '': params.append(param) # add parameter if its not empty
            target = model in MODELS.keys() # if the model is in the MODELS dict, we should simulate it later
            # note: we will simulate radiation effects on this device later only if "target" is true
            device = {'name':name,'pins':pins,'model':model,'params':params,'line':i,'target':target} # make dict
            devices.append(device) # add device to list of devices
    nets = list(set(nets)) # save unique nets
    return netlist,devices,list(set(nets))

def get_stimuli(devices,nets): # generate stimuli (list of lists of strings) based on devices and nets
    targets = []
    for device in devices: # for each device in device list
        if device['target']: targets.append(device) # if device is a simulation target
    inputs = [] # empty list to hold inputs
    for net in nets: # for each net
        if net in INPUT_ALIAS: inputs.append(net) # if input, add net to inputs
    stimuli = [] # create empty list of stimulis
    meta = [] # create empty list for meta data
    test = 0 # start test counter at 0
    for bias in itertools.product([False,True],repeat=len(inputs)): # for each bias condition
        for target in targets: # for each target device
            stimulus = [] # create empty stimulus file (in spectre syntax)
            stimulus.append(f'// SkySim test{test}') # add comment
            stimulus.append(f'// target device: {target["name"]}') # add comment
            conditions = ' '.join([f'{n}:{int(b)}' for n,b in zip(inputs,bias)])
            stimulus.append(f'// input conditions: {conditions}') # add comment
            meta.append({'test':test,'target':target['name'],'inputs':conditions}) # run meta data
            i = 0 # start input net counter at 0
            for net in nets: # for each net
                if net in VDD_ALIAS: stimulus.append(f'VDD ({net} 0) vsource dc={VDD}') # add VDD stimulus
                if net in VSS_ALIAS: stimulus.append(f'VSS ({net} 0) vsource dc={VSS}') # add VSS stimulus
                if net in INPUT_ALIAS: # if net is an input
                    if bias[i]: stimulus.append(f'V{i} ({net} 0) vsource dc={INPUT_HIGH}') # bias high
                    else: stimulus.append(f'V{i} ({net} 0) vsource dc={INPUT_LOW}') # bias low
                    i += 1 # incremenet input net counter
            nodes = [target['pins'][n] for n in MODELS[target['model']]] # find fault injector nodes
            settings = 'type=pulse val0=0 val1=200u period=100n width=5p rise=1p fall=5p' # fault injector setting
            stimulus.append(f'STRIKE ({nodes[0]} {nodes[1]}) isource ' + settings) # add fault injector stimulus
            #stimulus.append(f'CAP ({nodes[0]} {nodes[1]}) capacitor c=0.1n') # add capacitor
            #stimulus.append(f'DIODE ({nodes[1]} {nodes[0]}) pdiode area=6') # add diode
            stimulus.append('sim tran stop=100p') # define simulation type
            stimulus.append('') # empty line
            stimuli.append(stimulus) # add stimulus to list of stimuli
            test += 1
    return stimuli,pd.DataFrame(meta).set_index('test')

def format_bash(cell_path,tests):
    bash = [
        'MODELS="/home/PDKs/Skywater/V1.10.500/MODELS/SPECTRE/c9fh-3r/Models/"', # define models directory
        'source env/bin/activate' # activate SW/Python environment
    ]
    for test in tests: # for each test
        test_path = f'{cell_path}/test{test}' # get path to test directory
        bash.append(f'spectre {test_path}/input.scs -I/$MODELS -format psfascii -raw {test_path}') # run spectre
        bash.append(f'cp input.log {test_path}/input.log') # copy spectre log
        bash.append('rm -r input.ahdlSimDB input.log') # delete old spectre log
        bash.append(f'python3 scripts/analyze.py {test_path}') # process spectre output
    return '\n'.join(bash) # format bash file

def write_tests(cell_path,netlist,stimuli): # write spectre input files (netlist + stimulus)
    os.makedirs(cell_path,exist_ok=True) # make cell directory
    open(cell_path + '/netlist.scs','w').write('\n'.join(netlist)) # write netlist file
    for i in range(len(stimuli)): # for each stimulus file
        os.makedirs(cell_path + f'/test{i}',exist_ok=True) # make test directory
        open(cell_path + f'/test{i}/input.scs','w').write('\n'.join(netlist + stimuli[i])) # write netlist+stimulus
        open(cell_path + f'/test{i}/run.sh','w').write(format_bash(cell_path,[i])) # write bash run file
        os.chmod(cell_path + f'/test{i}/run.sh',0o775) # give bash file permissions
    open(cell_path + '/run_all.sh','w').write(format_bash(cell_path,range(len(stimuli)))) # write bash run_all file
    os.chmod(cell_path + '/run_all.sh',0o775) # give bash file permissions

def generate(cell_path): # generate tests for virtuoso cell
    # to do: generate virtuoso netlist from command line (instead of CIW)
    netlist,devices,nets = read_netlist(cell_path) # read cell netlist
    stimuli,meta = get_stimuli(devices,nets) # get stimulus files for test cases
    meta.to_csv(f'{cell_path}/meta.csv') # save test case meta data
    write_tests(cell_path,netlist,stimuli) # write simulation files
    print(f'\033[94mcommand to run all tests: \033[96m{cell_path}/run_all.sh\033[0m') # print run command

if __name__ == '__main__':
    if len(sys.argv) > 1: CELL_PATH = sys.argv[1]
    generate(CELL_PATH)