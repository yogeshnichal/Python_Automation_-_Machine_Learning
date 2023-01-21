import os
import sys
import time
import psutil
import logging as lg

def ProcInfo(Pro_Name):
    Prolst = psutil.process_iter()
    Name = []
    PID = []
    PUN = []
    PCM = []
    for i in Prolst:
        PSN = str(i.name()).lower()

        if Pro_Name.lower() == PSN:
            Name.append(str(i.name()))
            PID.append((str(i.pid)))
            try:
                PUN.append(str(i.username()))
            except Exception:
                PUN.append("Access Denied")
            try:
                PCM.append(str(i.memory_percent()))
            except Exception:
                PCM.append(str("Unable to get memory_percent"))

    if len(PID) > 0:
        FilePro = open("ProcessInfo.txt", "w")
        for i, j, k, l in zip(Pro_Name, PID, PUN, PCM):
            FilePro.writelines(i + "\n" + j + "\n" + k + "\n" + l + "\n")
        FilePro.close()
    else:
        lg.basicConfig(filename="Process_Log.txt", level=lg.DEBUG)
        lg.info("Process not running or Check file name")
        print("Process not running or Check file name")


def main():
    print("---------------------------Automation script by Yogesh Nichal---------------------------")
    print("\nApplication name: ", sys.argv[0])
    if len(sys.argv) != 2:
        lg.info("Invalid number of arguments. Use -h or -u options for help or usage")
        exit()

    if sys.argv[1].lower() == '-h':
        print("Script to display process information")

    if sys.argv[1].lower() == '-u':
        print("Usage: Application name Directory name")

    try:
        ProcInfo(sys.argv[1])

    except Exception as E:
        print("Error: Invalid input", E)

    finally:
        print("\n--------------------------------------Thank You--------------------------------------")


if __name__ == "__main__":
    main()