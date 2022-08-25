#!/bin/bash
source /usr/local/isde/cadence/bashrc.cadence
INDC=%INDC_PBS%
NODE=%NODE_PBS%
TIME=%TIME_PBS%
LET=%LET_PBS%

cat /home/loveletd/20080108_VCO_TMR/tmpl/vco_B_5stage_1_75-GHz_vN.tmpl | sed s/%LET%/$LET/g | sed s/%TIME%/$TIME/g | sed s/%NODE%/$NODE/g | sed s/%INDC%/$INDC/g > /home/loveletd/20080108_VCO_TMR/data/raw/vco_B_5stage_1_75-GHz_N_$NODE-LET$LET-$INDC-V-$TIME-per.scs

/usr/local/isde/cadence/IC5141/tools/bin/spectre /home/loveletd/20080108_VCO_TMR/data/raw/vco_B_5stage_1_75-GHz_N_$NODE-LET$LET-$INDC-V-$TIME-per.scs

python /home/loveletd/scripts/fixraw_tran.py /home/loveletd/20080108_VCO_TMR/data/raw/vco_B_5stage_1_75-GHz_N_$NODE-LET$LET-$INDC-V-$TIME-per.raw > /home/loveletd/20080108_VCO_TMR/data/sorted/vco_B_5stage_1_75-GHz_N_$NODE-LET$LET-$INDC-V-$TIME-per.raw.sorted

python /home/loveletd/scripts/analyzePLL.py /home/loveletd/20080108_VCO_TMR/data/sorted/vco_B_5stage_1_75-GHz_N_$NODE-LET$LET-$INDC-V-$TIME-per.raw.sorted 2 2 0 > /home/loveletd/20080108_VCO_TMR/phase_sweep_data/data_vco_B_5stage_1_75-GHz_N_$NODE-LET$LET-$INDC-V_$TIME-per.phase

\rm /home/loveletd/20080108_VCO_TMR/data/raw/vco_B_5stage_1_75-GHz_N_$NODE-LET$LET-$INDC-V-$TIME-per.raw

\rm /home/loveletd/20080108_VCO_TMR/data/sorted/vco_B_5stage_1_75-GHz_N_$NODE-LET$LET-$INDC-V-$TIME-per.raw.sorted

\rm /home/loveletd/20080108_VCO_TMR/data/raw/vco_B_5stage_1_75-GHz_N_$NODE-LET$LET-$INDC-V-$TIME-per.scs

\rm -r /home/loveletd/20080108_VCO_TMR/data/raw/vco_B_5stage_1_75-GHz_N_$NODE-LET$LET-$INDC-V-$TIME-per.ahdlcmi

#\rm /home/loveletd/20080108_VCO_TMR/sh/$NODE-$INDC-$TIME-$LET.sh

#\rm /home/loveletd/20080108_VCO_TMR/log/pbs_output$NODE-$INDC-$TIME-$LET.log
