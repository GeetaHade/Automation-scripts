#Task : use cmd line ags

import psutil
import time
import schedule
import os
import sys


def CreateLog(FolderName = "file6"):

    if not os.path.exists(FolderName):
        os.mkdir(FolderName)

    timestamp = time.ctime()
    timestamp = timestamp.replace(" ","")
    timestamp = timestamp.replace(":","_")
    timestamp = timestamp.replace("/","_")

    FileName = os.path.join(FolderName,"file%s.log" % (time.ctime())) 
    fd = open(FileName, "w")
    separator = "-"*70

    fd.write(separator + "\n")
    fd.write("Process log" + "\n")
    fd.write("Log file created at : "+time.ctime() + "\n")
    fd.write(separator + "\n")

    Arr = GetprocessInfo()

    for data in Arr:
        fd.write("%s \n" %data)
        
    
    fd.write(separator + "\n")
    fd.close()


def GetprocessInfo():
    listprocess = []
    for proc in psutil.process_iter(['pid', 'name', 'username']):
        listprocess.append(proc.info)

    return listprocess

def main():

    schedule.every(int(sys.argv[1])).minutes.do(CreateLog)

    while True:
        schedule.run_pending()
        time.sleep(1)

    

if __name__ == "__main__":
    main()