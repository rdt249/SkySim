# Ryan Young 2021

import os
import subprocess
import shutil
import sys
###################
#Global Parameters#
###################

#PART NAME
part = f"{sys.argv[1]}/" #SET PART NAME


#CONFIGURABLE PARAMETERS
VSS = 0
#VDD = [0.7, 0.8, 0.9, 1, 1.1, 1.2]
#TEMPS = [27, -196.15]
DVAL = [0, 1.2]
#STRIKES = ["n", "p", "nn", "pp"]
#TIME2 = [f"5.015n", f"5.02n", f"5.025n", f"5.03n", f"5.035", f"5.04n", f"5.045n", f"5.05n"]
#IPEAK = f"200u"
MODE = "SINGLE" #DOUBLE

#TEST PARAMETERS
IPEAK = f"300u"
TIME2 = [f"6n"]
VDD = [1.2]
TEMPS = [27]
#DVAL = [1.2]
STRIKES = ["n", "p"]

#CONSTANTS
models_home = f"/home/PDKs/Skywater/V1.8.0/MODELS/SPECTRE/c9fh-3r/"
cryo_path = f"CryoModels/"
room_temp_path = f"Models/"
bash_command_base = f"#!\nsource /home/young/SW_Run/bashrc.IC\n/usr/local/cadence/installs/SPECTRE191/tools/bin/spectre "
main_path = f"/home/young/SW_Run/TEST_SIMS/latches/"
main_folder = f"{main_path}{part}"
node_file = f"{main_folder}nodes.txt"
input_template = f"{main_folder}input.scs"
sim_main_folder = f"{main_folder}runs/{MODE}/"
data_folder = f"{main_folder}data/{MODE}/"
graphical_stimuli = f"_graphical_stimuli.scs"

#############################################################
#Build and places bash file specific to simulation iteration#
#############################################################
def buildBashFile(folder):
	bash_location = f"{sim_main_folder}{folder}/"
	bash_file = f"{bash_location}bash.sh"
	bash_command = f"{bash_command_base}{bash_location}{folder}.scs"
	run_file = open(bash_file, "w")
	run_file.write(bash_command)
	run_file.close()
	return bash_file

##########
#Simulate#
##########
def runSimulation(bash):
	subprocess.call(['sh', f"{bash}"])


def buildInputFile(t, v, d, s, n1, n2, folder, mode, time, IPEAK):
	f = open(f"{sim_main_folder}{folder}/{folder}.scs", "w")
	f.write(f"// Generated for: spectre\n")
	f.write(f"// Generated on: Jan 29 22:02:57 2021\n")
	f.write(f"// Design library name: Test_SW\n")
	f.write(f"// Design cell name: dfrtp1\n")
	f.write(f"// Design view name: schematic\n")
	f.write(f"simulator lang=spectre\nglobal 0\n")
	params = f"parameters IEXP={IPEAK} D={d} VHIGH={v} VLOW={VSS} TEMP={t}\n"
	f.write(params)
	if t == 27:
		model = f"{models_home}{room_temp_path}design_wrapper.lib"
	else:
		model = f"{models_home}{cryo_path}design_wrapper.lib"
	f.write(f"include \"{model}\" section=tt_fet\n")
	f.write(f"include \"{model}\" section=tt_rc\n")
	f.write(f"include \"{model}\" section=tt_parRC\n")
	f.write(f"include \"{model}\" section=tt_cell\n")
	f.write(f"include \"{model}\" section=models\n")
	for line in infile:
		if f"SAVEHERE" in line:
			if MODE == "DOUBLE":
				f.write(f"save I999:sink Q\n")
			else:
				f.write(f"save I999:sink Q\n")
			continue
				
		f.write(line)
		if f"graphical_stimuli" in line:
			if MODE == "DOUBLE":
				if s == f"p":
					p_node = f"({n1} vgnd)"
					n_node = f"(vpwr {n2})"
				elif s == "n":
					p_node = f"({n2} vgnd)"
					n_node = f"(vpwr {n1})"
				elif s == "pp":
					p_node = f"({n1} vgnd)"
					n_node = f"({n2} vgnd)"
				else:
					p_node = f"(vpwr {n2})"
					n_node = f"(vpwr {n1})"
				f.write(f"I999 {p_node} isource type=exp val0=0 val1=IEXP td1=5n tau1=2p td2={time} \\\n tau2=10p\n")
				f.write(f"I998 {n_node} isource type=exp val0=0 val1=IEXP td1=5n tau1=2p td2={time} \\\n tau2=10p\n")
			else:
				if s == f"p":
					cur_nodes = f"({n1} vgnd)"
				else:
					cur_nodes = f"(vpwr {n1})"
				f.write(f"I999 {cur_nodes} isource type=exp val0=0 val1=IEXP td1=5n tau1=2p td2={time} \\\n tau2=10p\n")
		
		
def createRunFolder(folder):
	try: os.mkdir(f"{sim_main_folder}{folder}")
	except: pass
	print(f"{sim_main_folder}/{folder}")
	src = f"{main_folder}{graphical_stimuli}"
	dst = f"{sim_main_folder}{folder}/{graphical_stimuli}"
	shutil.copyfile(src, dst)

###################################################################################
#Create iterable list of spectre nodes, and savable file/folder names ("." -> "-")#
###################################################################################
def getNodes(filename):
	node_def = []
	node_filename = []	
	f = open(filename)
	for line in f:
		node_def.append(line.strip())
		node = line.replace(".", "-")
		node_filename.append(node.strip())
	f.close()
	return node_def, node_filename


#Get template for input file construction
def getInputTemplate(file):
	temp = open(file, "r")
	lines = temp.readlines()
	temp.close()
	return lines

####################################################################
#Returns folder / file name (TEMP, VDD, D, STRIKE TYPE(s), NODE(s))#
####################################################################
def getRunName(t, v, d, s, n1, n2):
	if t == 27:
		model = f"ROOMT"
	else:
		model = f"CRYO"
	if MODE == "SINGLE":
		if s == "p":
			strike = f"PSTRIKE"
		else:
			strike = f"NSTRIKE"
		return f"{model}_{v}_{d}_{strike}_{n1}"
	elif MODE == "DOUBLE":
		if s == "p":
			strike1 = "PSTRIKE"
			strike2 = "NSTRIKE" #"NSTRIKE"
		elif s == "n":
			strike1 = "NSTRIKE"
			strike2 = "PSTRIKE" #"PSTRIKE"
		elif s == "pp":
			strike1 = "PSTRIKE"
			strike2 = "PSTRIKE" #"PSTRIKE"
			doubles[f"{strike2}{n2}{n1}{strike2}"] = 1
		elif s == "nn":
			strike1 = "NSTRIKE"
			strike2 = "NSTRIKE" #"PSTRIKE"
			doubles[f"{strike2}{n2}{n1}{strike2}"] = 1
		return f"{model}_{v}_{d}_{strike1}_{n1}_{strike2}_{n2}"
		

def cleanUp(folder):
	src = f"{sim_main_folder}{folder}/{folder}.raw"
	dst = f"{data_folder}{folder}.raw"
	shutil.copyfile(src, dst)
	os.remove(f"{main_path}{folder}.log")
	os.remove(f"{main_path}spectre.ic")
	os.remove(f"{main_path}spectre.fc")
	
###########	
#Main Loop#
###########		
def main():
	run_folder = getRunName(t, v, d, s, node_name1, node_name2)
	mylist = run_folder.split("_")
	if MODE == "DOUBLE":
		runname = f"{mylist[3]}{mylist[4]}{mylist[6]}{mylist[5]}"
		if runname in doubles:
			return
	createRunFolder(run_folder)
	bash_file = buildBashFile(run_folder)
	buildInputFile(t, v, d, s, n1, n2, run_folder, MODE, time, IPEAK)
	runSimulation(bash_file)
	cleanUp(run_folder)

###############	
#PROGRAM BEGIN#
###############
if __name__=="__main__":
	doubles = {}
	infile = getInputTemplate(input_template)
	nodes, node_file_names = getNodes(node_file)
	count = 0
	print("BEGIN")
	for t in TEMPS:
		for v in VDD:
			for d in DVAL:
				for s in STRIKES:
					for time in TIME2:
						for n1 in nodes:
							if MODE == "DOUBLE":
								for n2 in nodes:
									if n1 == n2:
										continue
									count += 1
									n1_index = nodes.index(n1)
									n2_index = nodes.index(n2)
									node_name1 = node_file_names[n1_index]
									node_name2 = node_file_names[n2_index]
									main()
									
							else:
								count += 1
								n2 = ""
								node_name2 = ""
								n1_index = nodes.index(n1)
								node_name1 = node_file_names[n1_index]
								main()
							#node_index = nodes.index(n)
							#node_name = node_file_names[node_index]
							#run_folder = getRunName(t, v, d, s, node_name)
							#createRunFolder(run_folder)
							#bash_file = buildBashFile(run_folder)
							#buildInputFile(t, v, d, s, n, run_folder, MODE)
							#runSimulation(bash_file)
	print(count)
	print(len(doubles))
	print(doubles)

	






