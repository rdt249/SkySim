MODELS="/home/PDKs/Skywater/V1.10.500/MODELS/SPECTRE/c9fh-3r/Models/"
source env/SW_Run/bashrc.IC
spectre data/MAINLIB_TESTING/SL_nand2/test14/input.scs -I/$MODELS -format psfascii -raw data/MAINLIB_TESTING/SL_nand2/test14
cp input.log data/MAINLIB_TESTING/SL_nand2/test14/input.log
rm -r input.ahdlSimDB input.log
python3 scripts/analyze.py MAINLIB_TESTING SL_nand2 test14