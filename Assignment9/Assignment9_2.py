import sys
import os.path

def main():

	if os.path.exists(sys.argv[1]):
		print("file exist")
	else:
		print("file dose not exist")
		exit()


	fd = open(sys.argv[1],'r')
	print("Display file:", fd)
	print("Content of file", fd.read())


if __name__ == "__main__":
	main()

# def ReadData(File):
# 	if os.path.exists(File):
# 		fd = open(File, "r")
# 		Data = fd.read()
# 		print("Data from the file:")
# 		print(Data)
# 		fd.close()
#
# 	else:
# 		print("File dose not exist")
#
#
# def main():
# 	Name = input("Enter the file name you want to read: ")
#
# 	ReadData(Name)
#
#
# if __name__ == "__main__":
# 	main()