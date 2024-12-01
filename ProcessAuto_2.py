import psutil

def CreateLog(FileName = "file1.log"):
    fd = open(FileName, "w")
    separator = "-"*70

    fd.write(separator + "\n")
    fd.write("Process Log"+"\n")
    fd.write(separator + "\n")

    fd.write("Contents of log file" + "\n")

    fd.close()

def main():
    CreateLog()

if __name__ == "__main__":
    main()