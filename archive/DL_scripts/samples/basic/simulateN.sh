#!/bin/bash

# Commands go here
cd /home/loveletd/20080108_VCO_TMR
INDC=%INDC%
NODE=%NODE%
TIME=%TIME%
LET=%LET%
#FREQ=%FREQ%
#cat run_sweep.sh | sed -e s/%INDC_PBS%/$INDC/g | sed -e s/%FREQ_PBS%/$FREQ/g > sh/$FREQ-$INDC.sh
cat run_sweepN.sh | sed s/%LET_PBS%/$LET/g | sed s/%TIME_PBS%/$TIME/g | sed s/%NODE_PBS%/$NODE/g | sed s/%INDC_PBS%/$INDC/g > sh/$NODE-$INDC-$TIME-$LET.sh
#bash sh/$FREQ-$INDC.sh
bash sh/$NODE-$INDC-$TIME-$LET.sh
