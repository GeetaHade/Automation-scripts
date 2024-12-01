import psutil
import time

def CreateLog(FileName = "File.log"):
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
    CreateLog()

if __name__ == "__main__":
    main()