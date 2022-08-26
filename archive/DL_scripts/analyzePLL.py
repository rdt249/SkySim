#!//usr/bin/python
  
#############################################################################
#to run: call python getFreq filename clkcolNumber vectorcolNumber startTime#
#############################################################################
#Description: this script reads a peridoc clock signal, and PLL (vector)    #
#output and determines the frequency, number of pulses, and jitter          #
#                                                                           #
#Author: Daniel Loveless (daniel.loveless@vanderbilt.edu                    #
#Last Update: 09/27/2007                                                    #
#############################################################################

import sys

datfile=sys.argv[1]          #filename
clockvec=sys.argv[2]         #column in file corresponding to the clock signal
vecnum=sys.argv[3]           #column in file corresponding to the output vector
starttime=float(sys.argv[4]) #start time for data comparison

print "\n" + datfile
thresh=600 #threshold voltage (0.5 VDD) for determining rising clock edges
tcol=0     #column in vector corresponding to the timestamps

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

     vec=[]    #vector for output data points
     cvec=[]   #vector for clock data points
     tvec=[]   #vector for time data points
     temp=0    #temp for vec
     clktemp=0 #temp for cvec
     ttemp=0   #temp for tvec
#     print vecnum
#     print len(line)
     #loop through the length of line (number of vectors in file)
     for i in range(len(line)):
           a=[] #vector to hold data from line
           a=line[i].split()

           #place appropriate data points in file in temps
           temp=float(a[int(vecnum)])
           clktemp=float(a[int(clockvec)])
           ttemp=float(a[int(tcol)])
           #append temp value to appropriate vectors
           vec.append(temp)
           cvec.append(clktemp)
           tvec.append(ttemp)
           
     ###########################################################################
     #find the rising edge of each clock pulse (used to determine the frequency)
     ###########################################################################

     flag=0      #flag for det if the last value was above or below threshold
     rise=0      #variable describing current value
     count=0     #counter incrementing every time a rising edge occurs
     tchk=[]     #vector for timestamps of each rising edge (50% point)
     numpulses=0 #the number of pulses (rising edges)

     for j in range(1,len(cvec)):        #loop through the clock vector
          rise=cvec[j]                   #assign the current value in vector
          if rise>=thresh:               #if the value is above the threshold
               if flag==0:               #and if the last value was below the th
                    count=count+1        #then incremnent the counter
                    tchk.append(tvec[j]) #and record the timestamp
               flag=1                    #flag=1 when the threshold is exceeded
          else:                          #if the value is below the threshold
               flag=0                    #set the flag back to 0

     numpulses=count                     #the number of pulses
     print "Total number of clock pulses:\t" + str(numpulses) 
     #print tchk
     ###########################################################################
     #           find the time difference between each timestamp               #
     ###########################################################################

     tdiff=[] #vector for the time differences between current and previous
     diff=0   #variable for time difference for current

     for k in range(2,count):    #loop through the timestamp vector
          diff=tchk[k]-tchk[k-1] #the time difference between pulses
          tdiff.append(diff)     #append the current value to a new vector

     ###########################################################################
     #average the resulting time diffs to get the per and freq (of clock data) #
     ###########################################################################

     sum=0     #sum of all time differences
     count=0   #counter (total number of differences)
     per=0     #the period of the signal
     freq=0    #the frequency of the signal (units Hz)
     freqMHz=0 #the frequency in units (MHz)

     for l in range(1,len(tdiff)): #loop through the vector of time differences
          sum=tdiff[l]+sum         #increment the sum of the values 

     print len(tdiff)       
     count=len(tdiff)              #the total number of values
     per=sum/count                 #the per is the avg of all of the time diffs
     freq=1/(per*1e-9)                    #frequency=1/period (Hz)
     freqMHz=round(freq/1e6)       #convert frequency into MHz
     print "Clock Frequency:\t" + str(freqMHz) + " MHz"

     ###########################################################################
     #             find the rising edge of each PLL output pulse               #
     ###########################################################################

     flag=0             #same as previous
     rise=0             #same as previous
     count=0            #counter for the total number of pulses
     countst=0          #count for the number of pulses following the start time
     tchk=[]            #vector for holding the timestamps of the pulses
     index=0            #count of the first pulse following the start time

     for m in range(1,len(vec)):         #loop through the vector of output data
          rise=vec[m]                    #set rise to current value in vector
          if rise>=thresh:               #if the value exceeds the threshold
               if flag==0:               #and the previous value was below th
                    count=count+1        #increment the number of pulses
                    tchk.append(float(tvec[m]))   #record the current timestamp
                    if float(tvec[m])>=starttime: #greater than the startime    
                         if index==0:             #and the 1st one 
                              index=count         #record which pulse number
                         countst=countst+1        #increment
               flag=1                             #threshold is exceeded        
          else:                                   #value is below the threshold
               flag=0                             #set the flag to 0

     print "Total number of vector pulses:\t" + str(count)	   
     print "Total number of vector pulses after " + str(starttime) + "s:\t" + str(countst)

     ###########################################################################
     #          find the time difference and the jitter of the signal          #
     ###########################################################################

     tdiff=[]  #vector for holding the time differences
     diff=0    #value of current difference
     sum=0     #sum of all time time differences
     sumd=0    #sum of residues (sum of (current tdiff-mean tdiff))
     jitter=0  #the average of the residues
     sqrd=0    #the sum of the sqaure of the residues
     std=0     #standard deviation of the sum of the squares 
     jitVal=0
     jitVec=[]

     for k in range(index+1,count):      #loop through the number of pulses
          diff=tchk[k]-tchk[k-1]         #find the time difference
          tdiff.append(diff)             #append the current tdiff to vectr
     for k in range(1,len(tdiff)):       #loop through the time differences
          sum=sum+tdiff[k]               #increment the sum of the differences
     mean=sum/len(tdiff)                 #find the average time difference
     for k in range(1,len(tdiff)):       #loop through the time differences
          jitVal=tdiff[k]-mean
          jitVec.append(jitVal)
          sumd=(tdiff[k]-mean)+sumd   #increment the sum of the residuals
          sqrd=((tdiff[k]-mean)**2)+sqrd #increment the sum of the squares
     print jitVec
     jitter=float(sumd/len(tdiff))       #average jitter
     sqrd=float(sqrd/len(tdiff))         #average of the sum of the squares
     std=sqrd**(0.5)                     #standard deviation
     jitter=jitter                 #average jitter in ps
     std=std                       #standard deviation of jitter in ps

     print "Jitter:\t" + str(jitter) + " ns +- " + str(std) + " ns\n"
