import os
from sys import *
from Checksum import *
import time
def DirDuplicateFilesRemoval(Dir_Path):
    flag = os.path.isabs(Dir_Path)
    if flag == False:
        Dir_Path = os.path.abspath(Dir_Path)

    exists = os.path.isdir(Dir_Path)
    data = {}
    if exists:
        for foldername, subfolder, filname in os.walk(Dir_Path):
            for subf in subfolder:
                print("Subfolder name of " + foldername + " is " + subf)
            print(" ")
            for fname in filname:
                fname = os.path.join(foldername, fname)
                checksum = hashfile(fname)

                if checksum in data:
                    data[checksum].append(fname)
                else:
                    data[checksum] = [fname]

        newdata = list(filter(lambda x: len(x) > 1, data.values()))
        Count = 0
        fd = open("Log.txt", 'w')
        for MainF in newdata:
            iCnt = 0
            for SubF in MainF:
                iCnt += 1
                if iCnt >= 2:
                    Count += 1
                    fd.write(SubF + "\n")
                    os.remove(SubF)
        print("Total Duplicate files ", Count)
        fd.close()
    else:
        print("Path is invalid ")


def main():
    print("-----------------YogeshNichal-----------------")
    print("\nApplication name:", argv[0])
    start = time.time()
    if len(argv) == 1:
        print("Error :invalid number of arguments")
        exit()
    if argv[1].lower() == '-h':
        print("This script will traverse the directory and delete all duplicate files from that directory.\n"
            "Script will write name of deleted files into a 'log' file and Log.txt will create into current directory\n"
            "and display execution time")
        exit()
    if argv[1].lower() == '-u':
        print("Usage: Application Name Demo name of directory")
        exit()

    try:
        DirDuplicateFilesRemoval(argv[1])
        end = time.time()
        print("time=", end-start)
    except FileNotFoundError:
        print("Error: Invalid input")
    except TypeError:
        print("Type Error: Positional argument")
    except ValueError:
        print("Error : Invalid datatype of input ")
    finally:
        print("\n""------------------Thank You------------------")


if __name__=="__main__":
    main()