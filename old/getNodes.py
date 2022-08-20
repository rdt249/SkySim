import os 
import sys


ignore_nodes = {"vpwr" : 1,
	"vpb" : 1,
	"vgnd" : 1,
	"vnb" : 1,
	"out" : 1}
	
ignore_parts = {"nshort" : 1,
	"pshort" : 1}

main_nodes = []

_ports = 0
_nodes = 1
_parts = 2

			
#returns false if at least 1 unique node, else true		
def ignoreCheck(ports, nodes):
	for node in nodes:
		if not node in ports:
			return False
	return True		
				
#returns instance name for given part	
def getInstance(line):
	instance = line.split()[0]
	return instance

#returns part name for given instance
def getPartName(lines, i):
	part_name = lines[i].split(")")[1].strip().split()[0]
	if part_name == f"\\":
		part_name = lines[i+1].strip()
	return part_name

#returns port definitions for given subckt
def getPorts(lines, i):
	port_line = lines[i]
	ports = port_line.split()[2:]
	if f"\\" in ports:
		ports.remove(f"\\")
		port_line = lines[i+1]
		ports = ports + port_line.split()
	return ports
	
	
#returns unique unique nodes, and instance(key) / part(item) dictionary	
def getNodes(lines, i):
	count = 0
	temp_node = []
	temp_inst = {}
	while True:
		line = lines[i]
		if "ends" in line:
			break
		if "(" in line:
			instance = getInstance(line)
			part = getPartName(lines, i)
			if not part in ignore_parts:
				temp_inst[instance] = part	
			nodes = line.split("(")[1].split(")")[0]
			for node in nodes.split():
				if node == f"\\":
					nodes = lines[i+1].split()
					for entry in nodes:
						if not entry in nodes:
							temp_node.append(entry)
				if not node in temp_node:
					temp_node.append(node)
		i += 1
		count += 1
	return temp_node, temp_inst, count

#returns subckt name
def getSubckt(line):
	ckt = line.split()[1]
	return ckt

#returns a dictionary with ports[0], nodes[1], and instances with names(dictionary)[2]
def getSubcktDefs(lines, max_line):
	subckts = {}
	ignore_ckts = []
	i = 0
	while True:
		if i >= max_line:
			break
		line = lines[i]
		if "//BEGIN" in line:
			break
		if "subckt" in line:
			ckt = getSubckt(line)
			ports = getPorts(lines, i)
			nodes, instances, plus_lines = getNodes(lines, i)
			t = []
			for entry in nodes:
				if not entry in ports:
					t.append(entry)
			i += plus_lines
			if ignoreCheck(ports, nodes):
				ignore_ckts.append(ckt)
			else:
				subckts[ckt] = [t, instances]
		else:
			i += 1
	return subckts, ignore_ckts, i

def getMain(lines, i):
	main = {}
	i += 1
	while True:
		line = lines[i]
		if f"_graphical_stimuli" in line:
			break
		inst = line.split()[0]
		part = line.split()[-1]
		main[inst] = part
		i += 1
	return main
		

def getSourceNodes(sub, inst, ckt, ignore, node):
	if ckt in ignore:
		return
	if node == "":
		node = inst
	else:
		node = f"{node}.{inst}"
		
	if not sub[ckt][1]:
		pass
	else:
		ins = sub[ckt][1]
		for item in ins:
			getSourceNodes(sub, item, ins[item], ignore, node)
	for net in sub[ckt][0]:
		main_nodes.append(f"{node}.{net}")

def main(folder, file):
	filename = f"{folder}/{file}"
	file = open(filename)
	lines = file.readlines()
	file.close()
	endLine = len(lines)
	subckts, ignore_list, i = getSubcktDefs(lines, endLine)
	mainckt = getMain(lines, i)
	for inst in mainckt:
		ckt = mainckt[inst]
		getSourceNodes(subckts, inst, ckt, ignore_list, "")
	outfile = open(f"{folder}/nodes.txt", "w")
	for node in main_nodes:
		outfile.write(f"{node}\n")
	outfile.close()
	print("NODE LIST CREATED")
	

if __name__=="__main__":
	folder = sys.argv[1]
	main(folder, f"input.scs")
	#outfile = open("output.txt" ,"w")
	#for entry in mydict:
		#outfile.write(f"{entry}___{mydict[entry]}\n")
	#outfile.close()
	#infile = open("output.txt", "r")
	#for line in infile:
	#	print(line)
	#	print(f"\n\n")
	#infile.close()

		
	



