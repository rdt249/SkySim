#!//usr/bin/python
import sys

datfile=sys.argv[1]
#datfile='full_circuit.raw'
infile=open(datfile,'r')

thresh=2.5
num_var=19  # 1+number of variables

dat=[]
a1=[]
tmpstr=''
k=0
line=' '
#for line in data:
val=0
tran=0
while line:
    line=infile.readline()
    if val and tran:

	linlist=line.split()
	for i in linlist:
#	dat.append(i)
	    #ii=str((int(float(i)*10000))/10000.0)
#	    if float(i)<0.001:
#		ii=str('%1.6e' % float(i))
#	    else:
#		ii=str('%1.3e' % float(i))

    	    tmpstr=tmpstr+i+' '
    	    if ((k+1) % num_var)==0 and not k==0:
#		a1.append(tmpstr)
		print tmpstr
		tmpstr=''
	    k+=1
    if line.find("DC")>=0:
	dc=1
    if line.find("Value")>=0 and dc==1:
	val=1
    if line.find("No. Variables")>=0 and dc==1:
	y=line.split()
	num_var=int(y[2])+1

infile.close()
    
