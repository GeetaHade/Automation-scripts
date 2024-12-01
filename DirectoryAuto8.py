#task1: take foldername from user and delete all files with size 0
#task2: output redirection: create a log file to store outpu ">"
#task3 : see if the ouput file name is not change the ouput is overwritten every time we run the code
#task4 : solution is to append to output to same efile which can be done by ">>"

import sys
import os
import time 

def DirectoryWatcher(DirName):

    flag = os.path.isabs(DirName) #used to check whether path is absolute

    if (flag == False):
        print("path is not absolute path")
        DirName = os.path.abspath(DirName) #used to convert relative path to absolute path
        print("converted absolute path is : ", DirName)
        

        
    exist = os.path.isdir(DirName) #method from os used to check if parameter is directory or not 

    if(exist == True):
        for foldername, subfoldername, filename in os.walk(DirName):
           
            for name in filename:
                if(os.path.getsize(os.path.join(foldername, name)) == 0):
                    os.remove(os.path.join(foldername, name))
                    print("Deleted file name : ", name)
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
            DirectoryWatcher(sys.argv[1])   #para to func is folder name
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


