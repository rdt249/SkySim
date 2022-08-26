#!

printf "\e[1;34m\tcopying input.scs...\n\e[1;m"
cp ~/simulation/$1/spectre/schematic/netlist/input.scs dev/input.scs

printf "\e[1;34m\tsetting up environment...\n\e[1;m"
source ~/SW_Run/bashrc.IC

printf "\e[1;34m\trunning spectre...\n\e[1;m"
MODELS="home/PDKs/Skywater/V1.10.500/MODELS/SPECTRE/c9fh-3r/Models/"
spectre dev/input.scs +escchars +log dev/spectre.out -I/$MODELS -format psfascii -raw dev +lqtimeout 900 -maxw 5 -maxn 5 +logstatus

printf "\e[1;34m\tcleaning up...\n\e[1;m"
rm -r input.ahdlSimDB
