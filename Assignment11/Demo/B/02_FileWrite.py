# File IO = File Input Output
import os.path

def WriteData(FileName):
    if(os.path.exists(FileName)):
        print("Enter the data that you want to write in the file")
        Data = input()

        with open(FileName, 'a') as fd:
            fd.write(f'\n{Data}')

    else:
        print("File is not existing")
        return


def main():
    print("Enter the file name to write")
    Name = input("File Name: ")

    WriteData(Name)


if __name__ == "__main__":
    main()