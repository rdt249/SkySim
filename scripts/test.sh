#!
# Stephen Lawrence 2022

source ~/SW_Run/bashrc.IC # set up cadence environment
mkdir $1 $1/netlist $1/psf # create directory for simulation inputs and results
cp ~/simulation/$1/spectre/schematic/netlist/input.scs $1/netlist/input.scs # copy netlist
cat template/simulate.scs >> $1/netlist/input.scs # create simulation instructions
MODELS="home/PDKs/Skywater/V1.10.500/MODELS/SPECTRE/c9fh-3r/Models/" # define path to models
spectre $1/netlist/input.scs -I/$MODELS -format psfascii -raw $1/psf # run spectre
cp input.log $1/netlist/input.log # copy log file to simulation directory
rm -r input.ahdlSimDB input.log # clean up unwanted files
printf "\e[1;34m\tdone. view results:\e[1;35m python3 scripts/plot.py ${1}\e[1;m\n"