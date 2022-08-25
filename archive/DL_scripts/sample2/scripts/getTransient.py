#!//usr/bin/python
  
#############################################################################
#to run: call python getTransient filename clkCol vectorcolNumber startTime #
#############################################################################
#Description: this script reads a .raw datafile and determines whether or   #   #             a DSET occured, and if so, the width of the transient         #
#                                                                           #
#Author: Daniel Loveless (daniel.loveless@vanderbilt.edu)                   #
#Last Update: 03/31/2008                                                    #
#############################################################################

import sys

datfile=sys.argv[1]          #filename
clkvecnum=sys.argv[2]        #column in file corresponding to clock vector
vecnum=sys.argv[3]           #column in file corresponding to the vector
starttime=float(sys.argv[4]) #start time for data comparison

print "\n" + datfile
thresh=0.6 #threshold voltage (0.5 VDD) for determining rising clock edges
tcol=1     #column in vector corresponding to the timestamps (default is 1)

#################
#import the file#
#################

IOflag=0

try:
     infile=open(datfile,'r')
     line=infile.readlines()
     infile.close()
except IOError, (errno, strerror):
     IOflag=1
     print "I/O error(%s): %s" % (errno, strerror)

if IOflag==0:
     ####################
     #grab the waveforms#
     ####################

     cvec=[]   #vector for clock data points
     vec=[]    #vector for output data points
     tvec=[]   #vector for time data points
     ctemp=0   #temp for cvec
     temp=0    #temp for vec
     ttemp=0   #temp for tvec
#     print vecnum
#     print len(line)
     #loop through the length of line (number of vectors in file)
     for i in range(len(line)):
           a=[] #vector to hold data from line
           a=line[i].split()

           #place appropriate data points in file in temps
           if clkvecnum==0:
           	ctemp=0
           else:
                ctemp=float(a[int(clkvecnum)])
           temp=float(a[int(vecnum)])
           ttemp=float(a[int(tcol)])
           #append temp value to appropriate vectors
           if clkvecnum==0:
                cvec=0
           else:
                cvec.append(ctemp)
           vec.append(temp)
           tvec.append(ttemp)

     ###########################################################################
     #find the rising edge of the transient (if exists) and timestamp          #
     ###########################################################################

     flag=0            #flag for det if the last value was above or below thresh
     rf=0              #variable describing current value
     count=0           #counter incrementing every time a rising edge occurs
     tchk=[]           #vector for timestamps of each rising edge (50% point)
     numpulses=0       #the number of pulses (rising edges)
     initVal=int(vec[0])    #the initial value of the datafile
     #print "Initial Value=\t" + str(initVal)
     if initVal==0:
          flag=0
     else:
          flag=1

     for j in range(1,len(vec)):       #loop through the clock vector
          if initVal==0:               #if looking for a pistive transient
               #print "Positve Transient"
               rf=vec[j]               #assign the current value in vector
               if flag==1:             #if the last value was above thresh
                    if rf<=thresh:     #if the current value is below thresh
                         count=count+1
                         tchk.append(tvec[j])
                         flag=0        #set flag back to 0
               else:                   #if last value was below thresh
                    if rf>=thresh:     #if the current value is above thresh
                         count=count+1 #then incremnent the counter
                         tchk.append(tvec[j]) #and record the timestamp
                         flag=1        #flag=1 when the threshold is exceeded
          else:                        #if looking for a negative transient
               #print "Negative Transient"
               rf=vec[j]               #assign the current value in vector
               if flag==0:              #if the last value was below thresh 
                    if rf>=thresh:     #if curent value is above thresh
                         count=count+1 #then increment counter
                         tchk.append(tvec[j]) #record timestamp
                         flag=1        #set flag back to 1
               else:                   #if last value is above thresh
                    if rf<=thresh:     #if current value is below thresh
                         count=count+1 #increment counter
                         tchk.append(tvec[j]) #record timestamp
                         flag=0        #set flag back to 0

     numpulses=(count-1)               #the number of pulses
     if numpulses==-1:
          numpulses=0

     print "Total number of transients:\t" + str(numpulses) 

     ###########################################################################
     #                       find the transient width                          #
     ###########################################################################

     tdiff=[] #vector for the time differences between current and previous
     diff=0   #variable for time difference for current

     for k in range(1,count):    #loop through the timestamp vector
          diff=tchk[k]-tchk[k-1] #the time difference between pulses
          tdiff.append(diff)     #append the current value to a new vector

     print "The transient width(s) are:\t" + str(tdiff)
     ###########################################################################
     #average the resulting time diffs to get the per and freq (of clock data) #
     ###########################################################################

#     sum=0     #sum of all time differences
#     count=0   #counter (total number of differences)
#     per=0     #the period of the signal
#     freq=0    #the frequency of the signal (units Hz)
#     freqMHz=0 #the frequency in units (MHz)

#     for l in range(1,len(tdiff)): #loop through the vector of time differences
#          sum=tdiff[l]+sum         #increment the sum of the values 

#     print len(tdiff)       
#     count=len(tdiff)              #the total number of values
#     per=sum/count                 #the per is the avg of all of the time diffs
#     freq=1/per                    #frequency=1/period (Hz)
#     freqMHz=round(freq/1e6)       #convert frequency into MHz
#     print "Clock Frequency:\t" + str(freqMHz) + " MHz"
#
     ###########################################################################     #             find the rising edge of each clock pulse                    #
     ###########################################################################

     flag=0             #same as previous
     rise=0             #same as previous
     count=0            #counter for the total number of pu
     countst=0          #count for the number of pulses following the start time
     fchk=[]            #vector for holding the timestamps of the pulses
     index=0            #count of the first pulse following the start time
     
     if clkvecnum==0:
          period=0
          freq=0
     else:
          for m in range(1,len(cvec)):      #loop through the vector of clk data
               rise=cvec[m]                 #set rise to current value in vector
               if rise>=thresh:             #if the value exceeds the threshold
                    if flag==0:             #and the previous value was below th
                         count=count+1      #increment the number of pulses
                         fchk.append(float(tvec[m])) #record the timestamp
                         if float(tvec[m])>=starttime: #greater than startime    
                              if index==0:           #and the 1st one 
                                   index=count       #record which pulse number
                              countst=countst+1      #increment
                    flag=1                           #threshold is exceeded        
               else:                                 #value is below the threshold
                    flag=0                           #set the flag to 0
          
          #print "Total number of vector pulses:\t" + str(count)	   
          #print "Total number of vector pulses after " + str(starttime) + "s:\t" + str(countst)
     
     ###########################################################################
     #               find the average clock frequency and period               #
     ###########################################################################
          
          fdiff=[]  #vector for holding the time differences
          diff=0    #value of current difference
          sum=0     #sum of all time time differences
          period=0  #average period (average time diffs)
          freq=0    #average frequency (1/period)
          
          for k in range(index+1,count):  #loop through the number of pulses
               diff=fchk[k]-fchk[k-1]     #find the time difference
               fdiff.append(diff)         #append the current fdiff to vectr
          
          for k in range(1,len(fdiff)):   #loop through the time differences
               sum=sum+fdiff[k]           #increment the sum of the differences
          
          if len(fdiff)==0:
               period=1
          else:
               period=(sum/len(fdiff))*1e9     #find the average time difference (ns)
          if period==0:
               period=1
          freq=(1/period)*1e3             #find the frequency (MHz)
    
          if period==1:
               period="NA"
               freq="NA" 
     
     print "Period of clock:\t" + str(period) + " ns"
     print "Clock frequency:\t" + str(freq) + " MHz"
