import sys
import time
import psutil

def ProcInfo():
    lst = []
    for i in psutil.process_iter():
        lst.append(i.as_dict(attrs=['name', 'pid', 'username']))

    fd1 = open("log.txt", 'w')
    fd1.write("Process information " + time.ctime())

    for i in lst:
        fd1.write("\n" + "-" * 80)
        fd1.write("\n" + str(i))

    for element in lst:
        fd1.write("%s\n" % element)


def main():
    print("---------------------------Automation script by Yogesh Nichal---------------------------")
    print("\nApplication name: ", sys.argv[0])
    if len(sys.argv) != 1:
        print("Invalid number of arguments. Use -h or -u options for help or usage")
        exit()

    try:
        ProcInfo()
    except IndexError:
        print("list index out of range")
    except Exception as E:
        print("Error: Invalid input", E)
    finally:
        print("\n--------------------------------------Thank You--------------------------------------")


if __name__ == "__main__":
    main()