def addition(N):
	N = sum(N)
	return N


def main():
	lst = []
	size = int(input("Enter size of list: "))

	for i in range(0, size):
		num = int(input("Enter list: "))
		lst.append(num)

	total = addition(lst)
	print("Addition of all elements:", total)


if __name__ == "__main__":
	main()
