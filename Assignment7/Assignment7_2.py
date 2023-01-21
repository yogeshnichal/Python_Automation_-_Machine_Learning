
import threading


def Evenfactor(No):
	Sum = 0

	for i in range(1, No):
		if No % i == 0 and i % 2 == 0:
			Sum += i
	print("Sum of EvanFactors is: {}".format(Sum))


def Oddfactors(No):
	Sum = 0

	for i in range(1, No):
		if No % i == 0 and i % 2 != 0:
			Sum += i
	print("Sum of OddFactors is: {}".format(Sum))


def ListFactors(No):
	Num = No
	lst = []

	for i in range(1, Num + 1):
		if Num % i == 0:
			lst.append(i)
	print("Factors are: {}".format(lst[:-1]))


def main():
	Num = int(input("Enter Number: "))

	T1 = threading.Thread(target=Evenfactor, args=(Num,))
	T2 = threading.Thread(target=Oddfactors, args=(Num,))
	T3 = threading.Thread(target=ListFactors, args=(Num,))

	T1.start()
	T2.start()
	T3.start()

	T1.join()
	T2.join()
	T3.join()

	print("exit from main")


if __name__ == "__main__":
	main()
