# File IO = File Input Output
import os.path

def DeleteData(FileName):
    if(os.path.exists(FileName)):
        os.remove(FileName)
    else:
        print("File is not exist")


def main():
    print("Enter the file name to Delete")
    Name = input("File Name: ")

    DeleteData(Name)


if __name__ == "__main__":
    main()