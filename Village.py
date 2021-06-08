import gzip
import os
import sys

lines 	= []
path = os.path.join(os.path.abspath("") + "\logs\\")
names = ["tidusrocks44","WiseOldMat","sauvanto","swo30"]

AllLogs = os.listdir(path)
AllLogs = AllLogs[:-1]

for i in range(len(AllLogs)):
	f=gzip.open(path + AllLogs[i],'rb')
	lines.append(f.readlines())


for x in range(len(lines)): #sorts through files 
	for y in range(len(lines[x])): #sorts through lines of file x 
		#for i in len(names):
		if "village" in lines[x][y] and "x" in lines[x][y] and "<" in lines[x][y]:
			sys.stdout.write(lines[x][y])
			sys.stdout.flush()
	


