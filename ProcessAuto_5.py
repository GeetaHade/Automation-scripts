#Task : Append output in generate log file

import psutil
import time
import schedule

def CreateLog(FileName = "File2.log"):
    fd = open(FileName, "a")
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

    schedule.every(1).minutes.do(CreateLog)

    while True:
        schedule.run_pending()
        time.sleep(1)

    

if __name__ == "__main__":
    main()