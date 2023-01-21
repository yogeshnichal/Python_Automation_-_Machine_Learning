import os
from sys import *

def ChkSum(Dir_Path):
	flag = os.path.isabs(Dir_Path)
	if flag == False:
		Dir_Path = os.path.abspath(Dir_Path)

	exists = os.path.isdir(Dir_Path)
	iCnt = 0

	if exists:
		for foldername, subfolder, filename in os.walk(Dir_Path):
		
			for subf in subfolder:
				print("Subfolder name of " + foldername + " is " + subf)
			print(" ")
			for fname in filename:
				print("File inside folder " + foldername + " is " + fname)
				iCnt += 1
		print(f"Total number of files is: {iCnt}")
	else:
		print("Path is invalid")


def main():
	print("-----------------YogeshNichal-----------------")
	print("\nApplication name:", argv[0])
	if len(argv) != 2:
		print("Insufficient arguments")
		exit()

	if argv[1].lower() == "-h":
		print("This script will traverse the directory and show count of files in directory")
		exit()

	if argv[1].lower() == "-u":
		print("Usage: Application Name Demo name of directory")
		exit()

	try:
		ChkSum(argv[1])
		exit()
	except FileNotFoundError:
		print("Error: Invalid input")
	except TypeError:
		print("Type Error: Positional argument")
	except ValueError:
		print("Not enough values")
	finally:
		print("\n""------------------Thank You------------------")


if __name__ == "__main__":
	main()