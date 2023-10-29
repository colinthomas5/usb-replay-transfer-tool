import os
from datetime import date
import shutil

def find_file(target, folder):
    for f in os.listdir(folder):
        path = os.path.join(folder, f)
        if os.path.isdir(path):
            result = find_file(target, path)
            if result is not None:
                return result
            continue
        if f == target:
            return path

drives = ['C:\\', 'D:\\', 'E:\\', 'F:\\', 'G:\\', 'H:\\', 'I:\\', 'J:\\', 'K:\\', 'L:\\', 'M:\\', 'N:\\', 'O:\\', 'P:\\', 'Q:\\', 'R:\\', 'S:\\', 'T:\\', 'U:\\', 'V:\\', 'W:\\', 'X:\\', 'Y:\\', 'Z:\\']
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') 
replayPath = os.path.join(desktop, "Console Slippi Replays")
if not os.path.exists(replayPath):
    os.makedirs(replayPath)
datePath = input("Enter the name of the new folder for replays to be dumped to (Leave blank for date): ")
if datePath == "":
    datePath = replayPath + "\\" + str(date.today())
if not os.path.exists(datePath):
    os.makedirs(datePath)
print("Replays to be dumped to " + datePath)
for drive in drives:
    if os.path.isdir(drive):
        filePath = os.path.join(drive, 'setup.info')
        slippiPath = os.path.join(drive, 'Slippi')
        if os.path.exists(filePath) and os.path.exists(slippiPath):
            print("Pulling replays off of the " + drive + " drive")
            setupNumber = open(filePath, 'r').read().lstrip('station=')
            if setupNumber == '0':
                setupPath = datePath + '\\Stream'
            else:
                setupPath = datePath + '\\Setup ' + setupNumber
            if not os.path.exists(setupPath):
                os.makedirs(setupPath)
            driveContents = os.listdir(slippiPath)
            for fileName in driveContents:
                if fileName.lower().endswith('.slp'):
                    checkPath = os.path.join(setupPath, fileName)
                    if os.path.exists(checkPath):
                        print("Skipping " + fileName + "; File already exists")
                    else:
                        oldPath = os.path.join(slippiPath, fileName)
                        shutil.copy2(oldPath, setupPath)
                        print("Copied over " + oldPath + " to " + setupPath)
            print("Finished pulling replays off of the " + drive + " drive")
deleteReplays = input("Replay copying finished. Would you like to delete the replays from the drives? (Y/N): ")
while deleteReplays != "Y" and deleteReplays != "y" and deleteReplays != "N" and deleteReplays != "n":
    print("Enter a valid response.")
    deleteReplays = input("Would you like to delete the replays from the drives? (Y/N): ")
if deleteReplays == "Y" or deleteReplays == "y":
    for drive in drives:
        if os.path.isdir(drive):
            filePath = os.path.join(drive, 'setup.info')
            slippiPath = os.path.join(drive, 'Slippi')
            if os.path.exists(filePath) and os.path.exists(slippiPath):
                print("Deleting replays from the " + drive + " drive")
                driveContents = os.listdir(slippiPath)
                for fileName in driveContents:
                    if fileName.lower().endswith('.slp'):
                        oldPath = os.path.join(slippiPath, fileName)
                        os.remove(oldPath)
                        print("Deleted " + oldPath)
                print("Finished deleting replays from the " + drive + " drive")
    input("Replay deleting finished. Press Enter or close the window.")
else:
    input("Press Enter or close the window.")
