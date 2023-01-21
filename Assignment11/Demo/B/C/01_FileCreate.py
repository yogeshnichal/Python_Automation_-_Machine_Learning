# File IO = File Input Output
import os.path
import re


def CreateFile(FileName):
    if(os.path.exists(FileName)):
        size = os.path.getsize(FileName)
        if (size == 0):
            fd = open(FileName, "w")
        else:
            print("ReWrite the file is already existing? Y/N")
            option = input()
            if (option == "Y" or option == "y"):
                with open(FileName, "w") as fd:
                    fd.write("")
    else:
        fd = open(FileName, "w")

def main():
    print("Enter the file name to create")
    Name = input("File Name: ")

    CreateFile(Name)


if __name__ == "__main__":
    main()