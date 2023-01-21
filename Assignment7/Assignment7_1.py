
import threading

def Even(No):
	for i in range(1, No, 1):
		if i % 2 == 0:
			print("Even number:", i)


def Odd(No):
	for i in range(1, No, 1):
		if i % 2 != 0:
			print("Odd number:", i)

def main():
	Num = 10

	T1 = threading.Thread(args=(Num,), target=Even )
	T2 = threading.Thread(target=Odd, args=(Num,))

	T1.start()
	T2.start()

	T1.join()
	T2.join()

	print("End of main")


if __name__ == "__main__":
	main()
