Y1=%Y1_SH%
Y0=%Y0_SH%
NODE=%NODE_SH%
HOMEPATH=/home/loveletd/20080331_GETTRANSIENT
#HOMEPATH=%HOMEPATH_SH%

if [ $Y0 -eq 1 ]
then
     
     Y00=1.2
else
     Y00=0
fi
if [ $Y1 -eq 1 ]
then
     
     Y11=1.2
else
     Y11=0
fi
if [ $Y2 -eq 1 ]
then
     
     Y22=1.2
else
     Y22=0
fi
if [ $Y3 -eq 1 ]
then
     
     Y33=1.2
else
     Y33=0
fi
if [ $X0 -eq 1 ]
then
     
     X00=1.2
else
     X00=0
fi
if [ $X1 -eq 1 ]
then
     
     X11=1.2
else
     X11=0
fi
if [ $X2 -eq 1 ]
then
     
     X22=1.2
else
     X22=0
fi
if [ $X3 -eq 1 ]
then
     
     X33=1.2
else
     X33=0
fi

cat $HOMEPATH/tmpl/nAdder.tmpl | sed s/%X3%/$X33/g | sed s/%X2%/$X22/g | sed s/%X1%/$X11/g | sed s/%X0%/$X00/g | sed s/%Y3%/$Y33/g | sed s/%Y2%/$Y22/g | sed s/%Y1%/$Y11/g | sed s/%Y0%/$Y00/g | sed s/%NODE%/$NODE/g > $HOMEPATH/data/raw/nAdder-X$X3$X2$X1$X0-Y$Y3$Y2$Y1$Y0-n$NODE.scs

/usr/local/isde/cadence/IC5141/tools/bin/spectre $HOMEPATH/data/raw/nAdder-X$X3$X2$X1$X0-Y$Y3$Y2$Y1$Y0-n$NODE.scs

python $HOMEPATH/scripts/fixraw_tran.py $HOMEPATH/data/raw/nAdder-X$X3$X2$X1$X0-Y$Y3$Y2$Y1$Y0-n$NODE.raw > $HOMEPATH/data/sorted/nAdder-X$X3$X2$X1$X0-Y$Y3$Y2$Y1$Y0-n$NODE.raw.sorted

for ((i=0; i<8; i=i+1))
do
     python $HOMEPATH/scripts/getTransient.py $HOMEPATH/data/sorted/nAdder-X$X3$X2$X1$X0-Y$Y3$Y2$Y1$Y0-n$NODE.raw.sorted 0 $((i+2)) 0 >> $HOMEPATH/sim_data/nAdder-X$X3$X2$X1$X0-Y$Y3$Y2$Y1$Y0-n$NODE.data
done

rm $HOMEPATH/data/raw/nAdder-X$X3$X2$X1$X0-Y$Y3$Y2$Y1$Y0-n$NODE.raw

#rm $HOMEPATH/data/sorted/nAdder-X$X3$X2$X1$X0-Y$Y3$Y2$Y1$Y0-n$NODE.raw.sorted

rm $HOMEPATH/data/raw/nAdder-X$X3$X2$X1$X0-Y$Y3$Y2$Y1$Y0-n$NODE.scs

rm -r $HOMEPATH/data/raw/nAdder-X$X3$X2$X1$X0-Y$Y3$Y2$Y1$Y0-n$NODE.ahdlcmi

#rm $HOMEPATH/sh/$NODE-X$X3$X2$X1$X0-Y$Y3$Y2$Y1$Y0.sh

#rm $HOMEPATH/log/pbs_output.log
