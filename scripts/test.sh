#!

FMT="\e[1;34m\t"
RST="\e[1;m\n"

printf "${FMT}setting up directory...${RST}"
mkdir $1 $1/netlist $1/psf

printf "${FMT}copying netlist...${RST}"
cp ~/simulation/$1/spectre/schematic/netlist/input.scs $1/netlist/input.scs

printf "${FMT}setting up simulation...${RST}"
cat template/simulate.scs >> $1/netlist/input.scs

printf "${FMT}setting up environment...${RST}"
source ~/SW_Run/bashrc.IC

printf "${FMT}running spectre...${RST}"
MODELS="home/PDKs/Skywater/V1.10.500/MODELS/SPECTRE/c9fh-3r/Models/"
spectre $1/netlist/input.scs +escchars +log $1/psf/spectre.out -I/$MODELS \
    -format psfascii -raw $1/psf +lqtimeout 900 -maxw 5 -maxn 5 +logstatus

printf "${FMT}cleaning up...${RST}"
rm -r input.ahdlSimDB

printf "${FMT}success!${RST}"
printf "${FMT}view results:\e[1;35m python3 scripts/plot.py ${1}${RST}"