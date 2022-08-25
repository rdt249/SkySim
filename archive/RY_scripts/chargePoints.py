import pickle


tmax = f"5.25n"
cmin = "200u"

qpoints = []

#tstep = .005
cstep = 20
#print(cstep)

#for i in range(1, 101):
	#qpoints.append([f"{round(5 + (i*tstep),3)}n", f"{cmin}"])
	
for i in range(1, 101):
	qpoints.append([tmax, f"{i*cstep}u"])
	
print(qpoints)
picklefile = open("chargepoints.pickle", "wb")
pickle.dump(qpoints, picklefile)
picklefile.close()
newq = open("chargepoints.pickle", "rb")
newlist = pickle.load(newq)

print(newlist)

