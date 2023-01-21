def frequency(N):
	N = (N)
	return N


def main():
	lst = []
	size = int(input("Enter size of list: "))
	frq = ''
	for i in range(0, size):
		num = int(input("Enter list: "))
		lst.append(num)
	times = int(input("Enter number for count: "))
	count = 0
	for i in range(size):
		if (lst[i] == times):
			count += 1

	total = frequency(lst)
	print("All list number:", total)
	print("Frequency: ", count)


if __name__ == "__main__":
	main()
