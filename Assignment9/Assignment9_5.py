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

	fname = sys.argv[1]
	txt = input("Find the word: ")
	Cnt = 0

	with open(fname, "r") as fd:
		for Data in fd:
			phrase = Data.split()
			for i in phrase:
				if i == txt:
					Cnt += 1
	print("Frequency of the  word:", Cnt)

	fd.close()


if __name__ == "__main__":
	main()
