#!/anaconda3/bin/python
import os
from datetime import datetime
from pync import Notifier
import time


def splitDateTime(dateTimeStr):
    splitted = dateTimeStr.split("-")
    return splitted[0], splitted[1], splitted[2]


def checkIfFolderExistsOrCreate(pathToFolder):
    if not os.path.exists(pathToFolder):
        os.makedirs(pathToFolder)


def checkFileEnding(file,possibleEndings):
    for end in possibleEndings:
        if file.endswith(end):
            return True
    return False

# home
dir = "/Users/taazuan3/Desktop"
cleanup = dir + "/cleanup"

# moved formats
format = ['.png','.jpg', '.mov']



os.chdir(dir)
checkIfFolderExistsOrCreate(cleanup)

counter = 0
for root, dirs, files in os.walk("."):
    for filename in files:
        if checkFileEnding(filename,format):
            if os.path.isfile(dir + "/" + filename):
                try:
                    dateTimeStr = datetime.utcfromtimestamp(os.path.getmtime(dir + "/" + filename)).strftime('%Y-%m-%d')
                    year, month, day = splitDateTime(dateTimeStr)
                    newPlace = cleanup + "/" + str(year) + "/" + str(month) + "/" + str(day)
                    checkIfFolderExistsOrCreate(newPlace)
                    os.rename(dir + "/" + filename, newPlace + "/" + filename)
                    print(filename)
                    counter += 1
                finally:
                    print("not found file " + filename)
if counter > 0:
    Notifier.notify('moved ' + str(counter) + " pictures to screenshot folder", title='Desktop Cleanup')
    time.sleep(10)
    Notifier.remove(os.getpid())
