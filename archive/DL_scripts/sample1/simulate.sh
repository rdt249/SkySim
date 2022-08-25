#!/bin/bash
#for NODE in I0.I76.net29 I0.net0150 I0.net082 I0.net083;
for NODE in `cat dpll90nm400MHz.nodes`
#for NODE in net011 
do
#cat pbs_output$NODE.log > test$NODE.test
#cat pbs_output$NODE.log| sed -n /fatal/p > test$NODE.test
#if [ -s cat pbs_output$NODE.log| sed -n /permission/p ]
#if [ -s test$NODE.test ]
#    then
#    cat pbs_output$NODE.log| sed -n /permission/p > test2$NODE.test    
#    cat test$NODE.test > test2$NODE.test
    cat simulate.pbs | sed s/%NODE%/$NODE/g | qsub
#fi 
#cat simulate.pbs | sed s/%NODE%/$NODE/g | qsub
done
#rm *.test
