#!//usr/bin/python

#########################################################
#to run script call python getFreq filename columnNumber#
#########################################################

######################################################################
#this script reads a peridoc clock signal and determins the frequency#
######################################################################

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
     ttemp=float(a[int(tcol)])
     tvec.append(ttemp)
#print tvec
####################################
#find the rising edge of each pulse#
####################################

flag=0
rise=0
count=0
tchk=[]

for j in range(1,len(vec)):
     rise=vec[j]
     if rise>=thresh:
          if flag==0:
               count=count+1
               tchk.append(tvec[j])
          flag=1
     else:
          flag=0

numpulses=len(tchk)

#################################################
#find the time difference between each timestamp#
#################################################

tdiff=[]
freqVEC=[]
tFreq=[]
diff=0
freq=0

for k in range(2,count):
     diff=tchk[k]-tchk[k-1]
     freq=1/diff
     tdiff.append(diff)
     freqVEC.append(freq)
     tFreq.append(tchk[k])

#########################################
#loop through lists and print in columns#
#########################################

freqval=0
timeval=0

#print len(freqVEC)
#print len(tFreq)
for l in range(1,len(freqVEC)):
     if l==1:
          print "Time \t Freq"
     freqval=tFreq[l]
     timeval=freqVEC[l]
     print str(freqval) + "\t" + str(timeval)
