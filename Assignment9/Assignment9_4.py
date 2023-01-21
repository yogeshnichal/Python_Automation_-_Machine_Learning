import sys
import os.path

if len(sys.argv) < 3:
	print("Insufficient arguments")
	print("Enter the filename using command line")
	exit()

def main():
	if os.path.exists(sys.argv[1]) and os.path.exists(sys.argv[2]):
		print("File exist")
	else:
		print("File dose not exist")
		exit()

	fd1 = open("Demo.txt", "r")
	fd2 = open("Hello.txt", "r")
	flag = False

	for Data1 in fd1:
		for Data2 in fd2:
			if Data1 == Data2:
				pass
			else:
				print("File contents not same")
				flag = True
			break
	fd1.close()
	fd2.close()

	if flag == False:
		print("File contents is same")


if __name__ == "__main__":
	main()
