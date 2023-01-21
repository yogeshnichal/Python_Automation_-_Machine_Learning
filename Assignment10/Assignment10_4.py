import os
from sys import *
from shutil import copyfile

def CopyAllExe(Dir_Path):
	flag = os.path.isabs(Dir_Path)
	if flag == False:
		Dir_Path = os.path.abspath(Dir_Path)

	exists = os.path.isdir(Dir_Path)

	if exists:
		os.mkdir(argv[2])
		flag = os.path.isabs(argv[2])
		if flag == False:
			pass
		for foldername, subfolder, filename in os.walk(Dir_Path):
			print("Current folder is: " + foldername)
			for subf in subfolder:
				print("Subfolder name of " + foldername + " is " + subf)
				for fname in filename:
					fd = fname.split(".")
					print(fname)

					newpath = os.path.abspath(argv[2])
					if fd[1] == argv[3][1:]:
						filepath = foldername
						source = os.path.join(filepath, fname)
						destination = os.path.join(newpath, fname)
						copyfile(source, destination)
					print("  ")

	else:
		print("Path is invalid")

def main():
	if len(argv) != 4:
		print("Insufficient arguments")
		exit()

	if argv[1].lower() == "-h":
		print("This script will traverse the directory and copy files to another directory")
		exit()

	if argv[1].lower() == "-u":
		print("Usage: Application Name AbsPath of Directory Copy .EXE to New Directory")
		exit()

	try:
		CopyAllExe(argv[1])
		exit()
	except FileNotFoundError:
		print("Error: Invalid input")


if __name__ == "__main__":
	main()
