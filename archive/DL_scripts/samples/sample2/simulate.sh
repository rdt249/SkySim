#!/bin/bash

# Commands go here
X3=%X3%
X2=%X2%
X1=%X1%
X0=%X0%
Y3=%Y3%
Y2=%Y2%
Y1=%Y1%
Y0=%Y0%
NODE=%NODE%
HOMEPATH=/home/loveletd/20080331_GETTRANSIENT
#HOMEPATH=%HOMEPATH%

cd $HOMEPATH
#echo $HOMEPATH
#echo "in simulate.sh"
cat run_scripts.sh | sed s/%X3_SH%/$X3/g |sed s/%X2_SH%/$X2/g | sed s/%X1_SH%/$X1/g | sed s/%X0_SH%/$X0/g | sed s/%Y3_SH%/$Y3/g | sed s/%Y2_SH%/$Y2/g | sed s/%Y1_SH%/$Y1/g | sed s/%Y0_SH%/$Y0/g | sed s/%NODE_SH%/$NODE/g > sh/$NODE-X$X3$X2$X1$X0-Y$Y3$Y2$Y1$Y0.sh

#sed s/%HOMEPATH_SH%/$HOMEPATH/g > sh/$NODE-X$X3$X2$X1$X0-Y$Y3$Y2$Y1$Y0.sh

bash sh/$NODE-X$X3$X2$X1$X0-Y$Y3$Y2$Y1$Y0.sh
