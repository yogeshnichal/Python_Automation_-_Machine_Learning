import sys
import os.path

if len(sys.argv) < 2:
	print("Insufficient arguments")
	print("Enter the filename using command line")
	exit()


def main():
	if os.path.exists(sys.argv[1]):
		print("File exist")
	else:
		print("File dose not exist")
		exit()

	with open(sys.argv[1]) as fd1:
		with open("Demo.txt", "w") as fd2:
			for Data in fd1:
				fd2.write(Data)
	fd1.close()


if __name__ == "__main__":
	main()
