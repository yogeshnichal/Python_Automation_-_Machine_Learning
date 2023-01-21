import os
from sys import *

def ChangeExt(Dir_Path):
	flag = os.path.isabs(Dir_Path)
	if flag == False:
		Dir_Path = os.path.abspath(Dir_Path)

	exists = os.path.isdir(Dir_Path)

	if exists:
		for foldername, subfolder, filename in os.walk(Dir_Path):
			print("Current folder is: " + foldername)
			for subf in subfolder:
				print("Subfolder name of " + foldername + " is: " + subf)
				for fname in filename:
					print(fname)

					filepath = foldername
					fd = fname.split(".")
					if fd[1] == argv[2][1:]:
						base = os.path.splitext(fname)[0]
						source = os.path.join(filepath, fname)
						destination = os.path.join(filepath, base + argv[3])
						os.rename(source, destination)
				print("  ")
				# exit()

	else:
		print("Path is invalid")


def main():
	if len(argv) != 4:
		print("Insufficient arguments")
		exit()

	if argv[1].lower() == "-h":
		print("This script will traverse the directory and display the changed extension")
		exit()

	if argv[1].lower() == "-u":
		print("Usage: Application Name AbsPath of Directory Old Extension New Extension")
		exit()

	try:
		ChangeExt(argv[1])
		exit()
	except FileNotFoundError:
		print("Error: Invalid input")


if __name__ == "__main__":
	main()
