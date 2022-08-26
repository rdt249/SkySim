#!/bin/bash
source /usr/local/cadence/bashrc.cadence
NODE=%NODE_PBS%
cat /home/loveletd/20060808_DPLL_scaling_study/dpll90nm400MHz.tmpl | sed s/%NODE%/$NODE/g >/home/loveletd/20060808_DPLL_scaling_study/dpll90nm400MHz_$NODE_10LET.scs
/usr/local/cadence/ic/tools/bin/spectre /home/loveletd/20060808_DPLL_scaling_study/dpll90nm400MHz_$NODE_10LET.scs
python /home/loveletd/scripts/fixraw_tran.py /home/loveletd/20060808_DPLL_scaling_study/dpll90nm400MHz_$NODE_10LET.raw > /home/loveletd/20060808_DPLL_scaling_study/data/sorted/dpll90nm400MHz_$NODE_10LET.raw.sorted
rm /home/loveletd/20060808_DPLL_scaling_study/dpll90nm400MHz_$NODE_10LET.raw
#mv /home/loveletd/20060808_DPLL_scaling_study/dpll90nm400MHz_$NODE.raw /home/loveletd/20060808_DPLL_scaling_study/data/raw/
