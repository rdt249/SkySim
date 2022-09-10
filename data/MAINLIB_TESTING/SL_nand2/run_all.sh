MODELS="/home/PDKs/Skywater/V1.10.500/MODELS/SPECTRE/c9fh-3r/Models/"
source env/SW_Run/bashrc.IC
spectre data/MAINLIB_TESTING/SL_nand2/test0/input.scs -I/$MODELS -format psfascii -raw data/MAINLIB_TESTING/SL_nand2/test0
cp input.log data/MAINLIB_TESTING/SL_nand2/test0/input.log
rm -r input.ahdlSimDB input.log
python3 scripts/analyze.py MAINLIB_TESTING SL_nand2 test0
spectre data/MAINLIB_TESTING/SL_nand2/test1/input.scs -I/$MODELS -format psfascii -raw data/MAINLIB_TESTING/SL_nand2/test1
cp input.log data/MAINLIB_TESTING/SL_nand2/test1/input.log
rm -r input.ahdlSimDB input.log
python3 scripts/analyze.py MAINLIB_TESTING SL_nand2 test1
spectre data/MAINLIB_TESTING/SL_nand2/test2/input.scs -I/$MODELS -format psfascii -raw data/MAINLIB_TESTING/SL_nand2/test2
cp input.log data/MAINLIB_TESTING/SL_nand2/test2/input.log
rm -r input.ahdlSimDB input.log
python3 scripts/analyze.py MAINLIB_TESTING SL_nand2 test2
spectre data/MAINLIB_TESTING/SL_nand2/test3/input.scs -I/$MODELS -format psfascii -raw data/MAINLIB_TESTING/SL_nand2/test3
cp input.log data/MAINLIB_TESTING/SL_nand2/test3/input.log
rm -r input.ahdlSimDB input.log
python3 scripts/analyze.py MAINLIB_TESTING SL_nand2 test3
spectre data/MAINLIB_TESTING/SL_nand2/test4/input.scs -I/$MODELS -format psfascii -raw data/MAINLIB_TESTING/SL_nand2/test4
cp input.log data/MAINLIB_TESTING/SL_nand2/test4/input.log
rm -r input.ahdlSimDB input.log
python3 scripts/analyze.py MAINLIB_TESTING SL_nand2 test4
spectre data/MAINLIB_TESTING/SL_nand2/test5/input.scs -I/$MODELS -format psfascii -raw data/MAINLIB_TESTING/SL_nand2/test5
cp input.log data/MAINLIB_TESTING/SL_nand2/test5/input.log
rm -r input.ahdlSimDB input.log
python3 scripts/analyze.py MAINLIB_TESTING SL_nand2 test5
spectre data/MAINLIB_TESTING/SL_nand2/test6/input.scs -I/$MODELS -format psfascii -raw data/MAINLIB_TESTING/SL_nand2/test6
cp input.log data/MAINLIB_TESTING/SL_nand2/test6/input.log
rm -r input.ahdlSimDB input.log
python3 scripts/analyze.py MAINLIB_TESTING SL_nand2 test6
spectre data/MAINLIB_TESTING/SL_nand2/test7/input.scs -I/$MODELS -format psfascii -raw data/MAINLIB_TESTING/SL_nand2/test7
cp input.log data/MAINLIB_TESTING/SL_nand2/test7/input.log
rm -r input.ahdlSimDB input.log
python3 scripts/analyze.py MAINLIB_TESTING SL_nand2 test7
spectre data/MAINLIB_TESTING/SL_nand2/test8/input.scs -I/$MODELS -format psfascii -raw data/MAINLIB_TESTING/SL_nand2/test8
cp input.log data/MAINLIB_TESTING/SL_nand2/test8/input.log
rm -r input.ahdlSimDB input.log
python3 scripts/analyze.py MAINLIB_TESTING SL_nand2 test8
spectre data/MAINLIB_TESTING/SL_nand2/test9/input.scs -I/$MODELS -format psfascii -raw data/MAINLIB_TESTING/SL_nand2/test9
cp input.log data/MAINLIB_TESTING/SL_nand2/test9/input.log
rm -r input.ahdlSimDB input.log
python3 scripts/analyze.py MAINLIB_TESTING SL_nand2 test9
spectre data/MAINLIB_TESTING/SL_nand2/test10/input.scs -I/$MODELS -format psfascii -raw data/MAINLIB_TESTING/SL_nand2/test10
cp input.log data/MAINLIB_TESTING/SL_nand2/test10/input.log
rm -r input.ahdlSimDB input.log
python3 scripts/analyze.py MAINLIB_TESTING SL_nand2 test10
spectre data/MAINLIB_TESTING/SL_nand2/test11/input.scs -I/$MODELS -format psfascii -raw data/MAINLIB_TESTING/SL_nand2/test11
cp input.log data/MAINLIB_TESTING/SL_nand2/test11/input.log
rm -r input.ahdlSimDB input.log
python3 scripts/analyze.py MAINLIB_TESTING SL_nand2 test11
spectre data/MAINLIB_TESTING/SL_nand2/test12/input.scs -I/$MODELS -format psfascii -raw data/MAINLIB_TESTING/SL_nand2/test12
cp input.log data/MAINLIB_TESTING/SL_nand2/test12/input.log
rm -r input.ahdlSimDB input.log
python3 scripts/analyze.py MAINLIB_TESTING SL_nand2 test12
spectre data/MAINLIB_TESTING/SL_nand2/test13/input.scs -I/$MODELS -format psfascii -raw data/MAINLIB_TESTING/SL_nand2/test13
cp input.log data/MAINLIB_TESTING/SL_nand2/test13/input.log
rm -r input.ahdlSimDB input.log
python3 scripts/analyze.py MAINLIB_TESTING SL_nand2 test13
spectre data/MAINLIB_TESTING/SL_nand2/test14/input.scs -I/$MODELS -format psfascii -raw data/MAINLIB_TESTING/SL_nand2/test14
cp input.log data/MAINLIB_TESTING/SL_nand2/test14/input.log
rm -r input.ahdlSimDB input.log
python3 scripts/analyze.py MAINLIB_TESTING SL_nand2 test14
spectre data/MAINLIB_TESTING/SL_nand2/test15/input.scs -I/$MODELS -format psfascii -raw data/MAINLIB_TESTING/SL_nand2/test15
cp input.log data/MAINLIB_TESTING/SL_nand2/test15/input.log
rm -r input.ahdlSimDB input.log
python3 scripts/analyze.py MAINLIB_TESTING SL_nand2 test15