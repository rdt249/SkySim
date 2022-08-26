#!

FMT="\e[1;34m\t"
RST="\e[1;m\n"

printf "${FMT}copying input.scs...${RST}"
cp ~/simulation/$1/spectre/schematic/netlist/input.scs dev/input.scs

printf "${FMT}setting up environment...${RST}"
source ~/SW_Run/bashrc.IC

printf "${FMT}running spectre...${RST}"
MODELS="home/PDKs/Skywater/V1.10.500/MODELS/SPECTRE/c9fh-3r/Models/"
spectre dev/input.scs +escchars +log dev/spectre.out -I/$MODELS -format psfascii -raw dev +lqtimeout 900 -maxw 5 -maxn 5 +logstatus

printf "${FMT}cleaning up...${RST}"
rm -r input.ahdlSimDB

printf "${FMT}success!${RST}"
