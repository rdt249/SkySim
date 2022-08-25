# Stephen Lawrence 2022

import subprocess
import os

# run configuration
RUN = {
    'dir':'dev',
    'lib':'MAINLIB_TESTING',
    'cell':'SL_nand2'
}

def ExportNetlist(): # export a netlist for a specified library and cell
    data = open('template/si.env','r').read() # start from template (based on File->Export->CDL...)
    data = data.replace('<LIB>',RUN['lib']) # replace placeholder with lib name
    data = data.replace('<CELL>',RUN['cell']) # replace placeholder with cell name
    open('~/SW_Run/si.env','w').write(data) # set up SW_Run to export netlist
    subprocess.call(['source','~/SW_Run/bashrc.IC']) # make sure we're in the right env
    subprocess.call(['si','-batch','-command','netlist']) # generate CDL netlist

def CloneNetlist():
    netlist = open('~/SW_Run/netlist','r').read()
    open(RUN['dir'] + '/netlist','w').write(netlist)
    return netlist

def FindNodes(netlist):
    for subckt in netlist.split('.SUBCKT'):
        subckt = subckt.split('.ENDS')[0]
        pins = subckt.split('\n')[0]

def CreateRun(run):
    ExportNetlist(run['lib'],run['cell'])
    netlist = CloneNetlist(RUN['dir'])
    RUN['nodes'] = FindNodes(netlist)

def main():
    print(0)

if __name__ == '__main__':
    main()