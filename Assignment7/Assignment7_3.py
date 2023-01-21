
import threading

def evenlist(iSize):
	lst = []

	for i in range(1, iSize):
		if i % 2 == 0:
			lst.append(i)
	print("Even list: {}\nSum of Even Numbers: {}".format(lst, sum(lst)))

def oddlist(iSize):
	lst = []

	for i in range(1, iSize):
		if i % 2 != 0:
			lst.append(i)
	print("Odd list: {}\nSum of Odd Numbers: {}".format(lst, sum(lst)))


def main():
	iSize = int(input("Enter Number: "))

	T1 = threading.Thread(target=evenlist, args=(iSize,))
	T2 = threading.Thread(target=oddlist, args=(iSize,))

	T1.start()
	T2.start()

	T1.join()
	T2.join()


if __name__ == "__main__":
	main()
