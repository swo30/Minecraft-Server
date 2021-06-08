import shutil
import time
from time import strftime, localtime
import os

number_players = 0
minecraft_path = os.path.abspath("") # gets current directory

def copyDirectory(src, dest):
	try:
		shutil.copytree(src, dest)
	# Directories are the same
	except shutil.Error as e:
		print('Directory not copied. Error: %s' % e)
	# Any error saying that the directory doesn't exist
	except OSError as e:
		print('Directory not copied. Error: %s' % e)

def ReadLogs(number_players):
    print(f"number of players: {number_players}")
    lines = []
    LogsPath = os.path.join(minecraft_path + "\\logs\\")
    
    with open(LogsPath + "latest.log", 'rb') as f:
        lines.append(f.readlines())

    for x in range(len(lines)): #sorts through files 
        for y in range(len(lines[x])): #sorts through lines of file x 
            lines[x][y] = (str(lines[x][y], 'utf-8'))
            if "joined the game" in lines[x][y]:
                number_players += 1
            if "lost connection: Disconnected" in lines[x][y] or "left the game" in lines[x][y]:
                number_players -= 1

    if number_players > 0:
        print("Someone in the server")
        return True
    else:
        print("No one in the server")
        return False


def DeleteOldBackup(num,path):
    Worlds = os.listdir(minecraft_path + "\Backups")
    if len(Worlds) > num:  #If more than num backups, delete oldest one
        shutil.rmtree( minecraft_path + "\Backups\\" + Worlds[0])



while True:
    if ReadLogs(number_players):
        print("Waiting for next backup interval")
        # time.sleep(60*120)
        date = strftime("%Y_%m_%d_%Hh%Mm%Ss", localtime())
        print(f"Backup created as {minecraft_path}\Backups\world_{date}")
        copyDirectory(minecraft_path + "\world", minecraft_path + "\Backups\world_"+ date)
        DeleteOldBackup(10, minecraft_path) #num =  number of backups to keep
    time.sleep(60)