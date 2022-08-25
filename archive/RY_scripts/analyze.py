import os
import sys
import shutil

part = sys.argv[1]
mode = sys.argv[2]
interrogation = False
qcol = 3
tcol = 1
PART_PATH = f"/home/young/SW_Run/TEST_SIMS/latches/{part}/"
MAIN_PATH = f"{PART_PATH}data/{mode}/"
RESULTS = f"{PART_PATH}{mode}_results.txt"
EXCLUDE = f"{PART_PATH}{mode}_exclude.txt"

def analyze(data, filename):
	dataline = float(filename.split("_")[2])
	event_flag = False
	thresh = 0.6
	if dataline == 0:
		flag = 0
	elif dataline == 1.2:
		flag = 1
	else:
		print(f"ERROR")
		return
	data_flag = False
	tvec = []
	for vec in data:
		if data_flag == False:
			if "Values" in vec:
				data_flag = True
			continue
		if interrogation == True:	
			if len(vec.split()) == 1:	
				Q = float(vec.split()[qcol])
			else:
				t = float(vec.split()[tcol])
		elif interrogation == False:
			Q = float(vec.split()[qcol])
			t = float(vec.split()[tcol])
		if t < float(3e-9):
			continue
		if flag == 0:
			if Q > thresh:
				tvec.append(t)
		else:
			if Q < thresh:
				tvec.append(t)
	if len(tvec) == 0:
		return False
	if max(tvec) - min(tvec) > float(0.35e-9):
		print(max(tvec) - min(tvec))
		return True
	else:
		return False
			
	


if __name__=="__main__":	
	rfile = open(RESULTS, "w")
	efile = open(EXCLUDE, "w")
	for f in os.listdir(MAIN_PATH):
		if "net" in f:
			continue
		datfile = f"{MAIN_PATH}{f}"
		file = open(datfile, "r")
		data = file.readlines()
		file.close()
		quitflag = analyze(data, f)
		if quitflag == True:
			rfile.write(f"{f[:-4]}\n")
		else:
			efile.write(f"{f[:-4]}\n")
	rfile.close()
	efile.close()
			
	
	
	
	
