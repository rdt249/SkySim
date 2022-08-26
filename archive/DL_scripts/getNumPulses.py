#!//usr/bin/python

#################################################################
#to run script call python getNumPulses.py filename columnNumber#
#################################################################

#############################################################################
#this script reads a peridoc clock signal and determins the number of pulses#
#############################################################################

import sys

datfile=sys.argv[1]
vecnum=sys.argv[2]

thresh=600
tcol=1

#################
#import the file#
#################

infile=open(datfile,'r')
line=infile.readlines()
infile.close()
#print line
###################
#grab the waveform#
###################

vec=[]
tvec=[]
temp=0
ttemp=0

for i in range(len(line)):
     a=[]
     a=line[i].split()
     temp=float(a[int(vecnum)])
     vec.append(temp)

####################################
#find the rising edge of each pulse#
####################################

flag=0
rise=0
count=0

for j in range(1,len(vec)):
     rise=vec[j]
     if rise>=thresh:
          if flag==0:
               count=count+1
          flag=1
     else:
          flag=0

numpulses=count
print numpulses
