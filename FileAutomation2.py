import sys


def Addition(A,B):
    return A+B


def main():
    print("----------------------------------------------")
    print("----------  Automation for adding-------------")
    print("----------------------------------------------")

    if(len(sys.argv) == 2):
        if (sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print(" This script is used to perform adddtition of 2 numbers")
            exit()

        if (sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Usage of script:")
            print("Name_of_file First_Argument Second Argument")
            print("Note : Both arguments are integers")
            exit()

        else:
            print("Invalid option")
            print("Use --h option to grt help and --u to get usage")

    if(len(sys.argv) == 3):
        try:
            ret = Addition(int(sys.argv[1]), int(sys.argv[2]))
            print("Addition is : ", ret)

        except ValueError as obj1:
            print("Invalid type of arguments")

        except Exception as obj2:
            print("unable to perform task due to ", obj2)

    else:
        print("invalid option")
        print("use --h option to get help use u to get usage")
        exit()
            
    


if __name__ == "__main__":
    main()