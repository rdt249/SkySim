import sys


def integrate(time, current):
	sum = 0
	for i in range(1, len(time)-1):
		t = time[i+1] - time[i]
		cur = 0.5 * abs(current[i+1] + current[i])
		sum += t * cur
	return sum	

def calculateLET(qcrit):
	siconstant = float(1.03e-14)
	LET = qcrit / siconstant
	return LET

def getQCrit(data, interrogate, ccol):
	time = []
	current = []
	if interrogate == True:
		for entry in data:
			line = entry.split()
			if len(line) == 1:
				continue
			else:
				time.append(float(entry.split()[1]))
				current.append(float(entry.split()[ccol]))
	return integrate(time, current)
		
if __name__=="__main__":
	filename = f"/home/young/SW_Run/6n1030u5-045n200u.raw"
	#filename = f"/home/young/SW_Run/ROOMT_0.7_0_NSTRIKE_I0-I6-I17-int1_PSTRIKE_I0-out-net17.raw"
	datfile = open(filename, "r")
	data = datfile.readlines()
	master = list(data)
	datfile.close()
	time = []
	current = []
	#Remove header information from data
	for entry in master:
		if f"value" in entry.lower():
			data.remove(entry)
			break
		else:
			data.remove(entry)
	for entry in data:
		if len(entry.split()) > 1:
			time.append(float(entry.split()[1]))
			current.append(float(entry.split()[2]))
		else:
			continue
	
	print(integrate(time, current))
	print(calculateLET(float(1.03e-12)))

		

