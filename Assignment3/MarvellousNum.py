def ChkPrime():
	lst = []
	size = int(input("Enter size of list: "))

	for i in range(0, size):
		num = int(input("Enter list: "))
		lst.append(num)
	count = 0
	for i in lst:
		num1 = 1
		for x in range(2,i):
			if i % x == 0:
				num1 = 0
				break
		if num1 == 1 and i != 0:
			count += i
	return count, lst
