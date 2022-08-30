#!
# Stephen Lawrence 2022

source ~/SW_Run/bashrc.IC # set up cadence environment
rm -r output/$1/$2 # remove old files
mkdir -p output/$1/$2/netlist output/$1/$2/psf # create directory for sim
cp ~/simulation/$1/spectre/schematic/netlist/input.scs output/$1/$2/netlist/input.scs # copy netlist
cat input/$1/$2.scs >> output/$1/$2/netlist/input.scs # create simulation instructions
MODELS="home/PDKs/Skywater/V1.10.500/MODELS/SPECTRE/c9fh-3r/Models/" # define path to models
spectre output/$1/$2/netlist/input.scs -I/$MODELS -format psfascii -raw output/$1/$2/psf # run spectre
cp input.log output/$1/$2/netlist/input.log # copy log file to simulation directory
rm -r input.ahdlSimDB input.log # clean up unwanted files
printf "\e[1;34m\tview results:\e[1;35m python3 scripts/plot.py $1 $2\e[1;m\n"