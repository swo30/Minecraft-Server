import gzip
import os
import sys

lines 	= []
minecraft 	= os.path.abspath("") # gets current directory
path 	= os.path.join(minecraft + "\\logs\\")
AllLogs = os.listdir(path)
AllLogs = AllLogs[:-1]

for i in range(len(AllLogs)):
	f=gzip.open(path + AllLogs[i],'rb')
	lines.append(f.readlines())

def DeathCounter(name):
	DeathCount = 0
	ExcludeNames = ["tidusrocks44","WiseOldMat","sauvanto","swo30"]
	if name in ExcludeNames: ExcludeNames.remove(name)

	for x in range(len(lines)): #sorts through files 
		for y in range(len(lines[x])): #sorts through lines of file x 
			if name in lines[x][y]:
				if "advancement" not in lines[x][y]:
					if "UUID" not in lines[x][y]:
						if "joined" not in lines[x][y]:
							if "logged" not in lines[x][y]:
								if "left" not in lines[x][y]:
									if "connection" not in lines[x][y]:
										if "<" not in lines[x][y]:
											if "moved" not in lines[x][y]: 
												if "completed" not in lines[x][y]: 
													if "game" not in lines[x][y]: 
														if ExcludeNames[0] not in lines[x][y]:
															if ExcludeNames[1] not in lines[x][y]:
																if ExcludeNames[2] not in lines[x][y]:
																	sys.stdout.write(lines[x][y])
																	sys.stdout.flush()
																	DeathCount = DeathCount + 1
	return DeathCount


Player = raw_input("Type the name of the player to find out his Death Count: ")
print(Player + " has died " + str(DeathCounter(Player)) + " times.")