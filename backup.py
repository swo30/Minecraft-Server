import datetime
import shutil
import time
# from time import strftime, localtime
import os
import sys
from unittest.mock import patch

NUM_BACKUP = 5
BACKUP_INTERVAL = 2  # In hours
number_players = 0
minecraft_path = os.path.abspath("")
_os_path_isfile = os.path.isfile

if sys.platform == 'linux':
    slash = '/'
else:
    slash = '\\'


def accept(path):
    if path in [f"session.lock"]:  # ignores session.lock and prevents crashes on windows
        print("skipping %r" % path)
        return False
    return _os_path_isfile(path)


def zip_folder(src, dest):
    with patch("os.path.isfile", side_effect=accept):
        shutil.make_archive(dest, "zip", src)


def read_logs(players):
    lines = []
    logs_path = os.path.join(f"{minecraft_path}{slash}logs{slash}")

    with open(logs_path + "latest.log", 'rb') as f:
        lines.append(f.readlines())

    for x in range(len(lines)):  # sorts through files 
        for y in range(len(lines[x])):  # sorts through lines of file x 
            lines[x][y] = (str(lines[x][y], 'utf-8'))
            if "joined the game" in lines[x][y]:
                players += 1
            if "left the game" in lines[x][y]:
                players -= 1
                if players < 0:
                    players = 0  # prevents negative player numbers
    print(f"There are currently {players} players in the server.")
    return players


def delete_old_backup(num):
    worlds = os.listdir(f"{minecraft_path}{slash}Backups{slash}")
    if len(worlds) > num:
        shutil.rmtree(f"{minecraft_path}{slash}Backups{slash}{worlds[0]}")


while True:
    number_players = read_logs(number_players)
    if number_players > 0:
        current_time = datetime.datetime.now()
        backup_time = current_time + datetime.timedelta(hours=BACKUP_INTERVAL)
        print(f"Next backup scheduled at {backup_time.hour:02d}:{backup_time.minute:02d}")
        # time.sleep(60 * 60 * BACKUP_INTERVAL)
        print(f"Starting backup...")
        current_time_string = f"{current_time.year}_{current_time.month:02d}_{current_time.day:02d}_{current_time.hour:02d}h_{current_time.minute:02d}m"
        zip_folder(f"{minecraft_path}{slash}world", f"{minecraft_path}{slash}Backups{slash}world_{current_time_string}")
        print(f"Backup created as {minecraft_path}{slash}Backups{slash}world_{current_time_string}")
        delete_old_backup(NUM_BACKUP)

    time.sleep(60)
