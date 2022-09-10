#!
# Stephen Lawrence 2022

MODELS='/home/PDKs/Skywater/V1.10.500/MODELS/SPECTRE/c9fh-3r/Models/' # define path to models
source ~/SW_Run/bashrc.IC # set up python and cadence environment
spectre data/$1/$2/$3/input.scs -I/$MODELS -format psfascii -raw data/$1/$2/$3 # run spectre
cp input.log data/$1/$2/$3/input.log # copy log file to simulation directory
rm -r input.ahdlSimDB input.log # clean up unwanted files
# printf "\e[1;34m\tview results:\e[1;35m python3 scripts/plot.py $1 $2\e[1;m\n"