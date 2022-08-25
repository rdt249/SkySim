#!//usr/bin/python
import sys

datfile=sys.argv[1]
infile=open(datfile,'r')

dat=[]
tran=0
tempInt=0
tempFloat=0
tranWidth=0
a=0
b=0
line=' '

while line:
     line=infile.readline()
     a=line.find("transients")
     print a
     if a>-1:
          linelist=line.split()
          tempInt=int(linelist[4])
          tran=tran+tempInt
          b=line.find("width(s)")
          print b
          if b>-1:
               linelist=line.split()
               tempFloat=linelist[4]
               print tempFloat
          else:
               tempFloat=0
#     tranWidth=tempFloat

print datfile + ":\t" + str(tran) + ":\t" + str(tempFloat)

infile.close()    
