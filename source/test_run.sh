#!

echo "copying input.scs ..."
cp ~/simulation/$1/spectre/schematic/netlist/input.scs dev/input.scs

echo "setting up environment ..."
source ~/SW_Run/bashrc.IC

echo "running spectre ..."
$MODELS = home/PDKs/Skywater/V1.10.500/MODELS/SPECTRE/c9fh-3r/Models/
spectre dev/input.scs -I/$MODELS -raw dev
