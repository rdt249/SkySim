MODELS="/home/PDKs/Skywater/V1.10.500/MODELS/SPECTRE/c9fh-3r/Models/"
source env/bin/activate
spectre MAINLIB_TESTING/SL_inv_1x/test0/input.scs -I/$MODELS -format psfascii -raw MAINLIB_TESTING/SL_inv_1x/test0
cp input.log MAINLIB_TESTING/SL_inv_1x/test0/input.log
rm -r input.ahdlSimDB input.log
python3 scripts/analyze.py MAINLIB_TESTING/SL_inv_1x/test0
spectre MAINLIB_TESTING/SL_inv_1x/test1/input.scs -I/$MODELS -format psfascii -raw MAINLIB_TESTING/SL_inv_1x/test1
cp input.log MAINLIB_TESTING/SL_inv_1x/test1/input.log
rm -r input.ahdlSimDB input.log
python3 scripts/analyze.py MAINLIB_TESTING/SL_inv_1x/test1
spectre MAINLIB_TESTING/SL_inv_1x/test2/input.scs -I/$MODELS -format psfascii -raw MAINLIB_TESTING/SL_inv_1x/test2
cp input.log MAINLIB_TESTING/SL_inv_1x/test2/input.log
rm -r input.ahdlSimDB input.log
python3 scripts/analyze.py MAINLIB_TESTING/SL_inv_1x/test2
spectre MAINLIB_TESTING/SL_inv_1x/test3/input.scs -I/$MODELS -format psfascii -raw MAINLIB_TESTING/SL_inv_1x/test3
cp input.log MAINLIB_TESTING/SL_inv_1x/test3/input.log
rm -r input.ahdlSimDB input.log
python3 scripts/analyze.py MAINLIB_TESTING/SL_inv_1x/test3