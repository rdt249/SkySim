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
indc=sys.argv[3]

thresh=sys.argv[4]
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
#print tchk
numpulses=len(tchk)
#print numpulses

#################################################
#find the time difference between each timestamp#
#################################################

tdiff=[]
diff=0

for k in range(2,count):
     diff=tchk[k]-tchk[k-1]
     tdiff.append(diff)

#print tdiff
##########################################################
#average the resulting time differences to get the period#
##########################################################

sum=0
count=0
per=0
freq=0

for l in range(1,len(tdiff)):
     sum=tdiff[l]+sum
     count=count+1

per=sum/count
freq=round(1/per * 1e-6)

indc = float(indc)
if indc==0:
     print "DC_IN (V)\t" + "Freq (MHz)" 
print str(indc) + "\t" + str(freq) 
