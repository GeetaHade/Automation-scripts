import psutil
import time

def CreateLog(FileName = "File.log"):
    fd = open(FileName, "w")
    separator = "-"*70

    fd.write(separator + "\n")
    fd.write("process log" + "\n")
    fd.write("log file created at : " + time.ctime() + "\n")
    fd.write(separator + "\n")

    fd.write(separator + "\n")

    fd.close()

def main():
    CreateLog()

if __name__ == "__main__":
    main()