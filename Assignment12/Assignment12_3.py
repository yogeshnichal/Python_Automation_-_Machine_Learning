import os
import sys
import time
import psutil

def ProcInfo(Dir_Name):
    lst = []
    for i in psutil.process_iter():
        lst.append(i.as_dict(attrs=['name', 'pid', 'username']))

    if os.path.isdir(Dir_Name) == False:
        os.mkdir(Dir_Name, mode=777)

    if os.path.isabs(Dir_Name) == False:
        Dir_Name = os.path.abspath(Dir_Name)

    filename = Dir_Name + "\log.txt"
    fd1 = open(filename, 'w')

    fd1.write("Process information " + time.ctime())

    for i in lst:
        fd1.write("\n" + "-" * 80)
        fd1.write("\n" + str(i))

    fd1.close()
    return filename


def main():
    print("---------------------------Automation script by Yogesh Nichal---------------------------")
    print("\nApplication name: ", sys.argv[0])
    if len(sys.argv) != 2:
        print("Invalid number of arguments. Use -h or -u options for help or usage")

    elif sys.argv[1].lower() == '-h':
        print("Script to display process information")

    elif sys.argv[1].lower() == '-u':
        print("Usage: Application name Directory name")

    try:
        ProcInfo(sys.argv[1])
    except IndexError:
        print("list index out of range")
    except Exception as E:
        print("Error: Invalid input", E)
    finally:
        print("\n--------------------------------------Thank You--------------------------------------")


if __name__ == "__main__":
    main()