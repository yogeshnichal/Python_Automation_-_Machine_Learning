def minimum(N):
	N = min(N)
	return N


def main():
	lst = []
	size = int(input("Enter size of list: "))

	for i in range(0, size):
		num = int(input("Enter list: "))
		lst.append(num)

	fix = minimum(lst)
	print("Minimum number from list:", fix)


if __name__ == "__main__":
	main()
