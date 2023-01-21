import os
from sys import *

def DirFilesDisplay(Dir_Path):
	flag = os.path.isabs(Dir_Path)
	if flag == False:
		Dir_Path = os.path.abspath(Dir_Path)

	exists = os.path.isdir(Dir_Path)
	
	if exists:
		for foldername, subfolder, filename in os.walk(Dir_Path):
		
			for subf in subfolder:

				for fname in filename:
					fd = fname.split(".")

					if fd[1] == argv[2][1:]:
						print("File with extension" + argv[2] + " inside " + foldername + " is " + fname)
				print("  ")
	else:
		print("Path is invalid")


def main():
	if len(argv) != 3:
		print("Insufficient arguments")
		exit()

	if argv[1].lower() == "-h":
		print("This script will traverse the directory and display the file extension")
		exit()

	if argv[1].lower() == "-u":
		print("Usage: Application Name AbsPath of Directory File Extension")
		exit()

	try:
		DirFilesDisplay(argv[1])
	except FileNotFoundError:
		print("Error: Invalid input")


if __name__ == "__main__":
	main()
