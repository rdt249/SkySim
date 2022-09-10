#!
# Stephen Lawrence 2022

# rm -r output/$1/$2 # remove old files
# mkdir -p output/$1/$2/netlist output/$1/$2/psf # create directory for sim
# cp ~/simulation/$1/spectre/schematic/netlist/input.scs input/$1/netlist.scs # copy netlist
# cp ~/simulation/$1/spectre/schematic/netlist/input.scs output/$1/$2/netlist/input.scs # copy netlist
# /usr/bin/python3 scripts/generate.py $1 # generate sim instructions
# cat input/$1/$2.scs >> output/$1/$2/netlist/input.scs # create simulation instructions

MODELS='/home/PDKs/Skywater/V1.10.500/MODELS/SPECTRE/c9fh-3r/Models/' # define path to models
source ~/SW_Run/bashrc.IC # set up python and cadence environment
# spectre output/$1/$2/netlist/input.scs -I/$MODELS -format psfascii -raw output/$1/$2/psf # run spectre
spectre data/$1/$2/$3/input.scs -I/$MODELS -format psfascii -raw data/$1/$2/$3 # run spectre
cp input.log data/$1/$2/$3/input.log # copy log file to simulation directory
rm -r input.ahdlSimDB input.log # clean up unwanted files
# printf "\e[1;34m\tview results:\e[1;35m python3 scripts/plot.py $1 $2\e[1;m\n"