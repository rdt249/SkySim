MODELS="/home/PDKs/Skywater/V1.10.500/MODELS/SPECTRE/c9fh-3r/Models/"
source env/SW_Run/bashrc.IC
spectre data/MAINLIB_TESTING/SL_inv_1x/test0/input.scs -I/$MODELS -format psfascii -raw data/MAINLIB_TESTING/SL_inv_1x/test0
cp input.log data/MAINLIB_TESTING/SL_inv_1x/test0/input.log
rm -r input.ahdlSimDB input.log
python3 scripts/analyze.py MAINLIB_TESTING SL_inv_1x test0
spectre data/MAINLIB_TESTING/SL_inv_1x/test1/input.scs -I/$MODELS -format psfascii -raw data/MAINLIB_TESTING/SL_inv_1x/test1
cp input.log data/MAINLIB_TESTING/SL_inv_1x/test1/input.log
rm -r input.ahdlSimDB input.log
python3 scripts/analyze.py MAINLIB_TESTING SL_inv_1x test1
spectre data/MAINLIB_TESTING/SL_inv_1x/test2/input.scs -I/$MODELS -format psfascii -raw data/MAINLIB_TESTING/SL_inv_1x/test2
cp input.log data/MAINLIB_TESTING/SL_inv_1x/test2/input.log
rm -r input.ahdlSimDB input.log
python3 scripts/analyze.py MAINLIB_TESTING SL_inv_1x test2
spectre data/MAINLIB_TESTING/SL_inv_1x/test3/input.scs -I/$MODELS -format psfascii -raw data/MAINLIB_TESTING/SL_inv_1x/test3
cp input.log data/MAINLIB_TESTING/SL_inv_1x/test3/input.log
rm -r input.ahdlSimDB input.log
python3 scripts/analyze.py MAINLIB_TESTING SL_inv_1x test3