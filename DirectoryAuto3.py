import sys
import os
import time 

def DirectoryWatcher(DirName):

    flag = os.path.isabs(DirName)

    if (flag == False):
        DirName = os.path.abspath(DirName)

        
    exist = os.path.isdir(DirName) #method from os used to check if parameter is directory or not 

    if(exist == True):
        for foldername, subfoldername, filename in os.walk(DirName):
            for name in filename:
                print(name)
    ¯
    else:
        print("There is no such directory")



def main():
    print("--------------------------------------------------")
    print("---------------Directory Watcher------------------")
    print("--------------------------------------------------")

    if (len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This script is used for directory traversal")
            exit()
        
        if(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Usage of script")
            print("Name_of_File    Name_of_Directory")
            exit()

        try:
            starttime = time.time()
            DirectoryWatcher(sys.argv[1])
            endtime = time.time()

            print("Time required to execute the script : ", endtime-starttime)

        except Exception as obj2:
            print("Unable to perform task due to", obj2)
    
    else:
        print("Invalid option")
        print("Use --h option to get help and use --u option to gt usage")
        exit()

    print("--------------------------------------------------")
    print("-----------Script execution successful------------")
    print("--------------------------------------------------")    

if __name__ == "__main__":
    main()


