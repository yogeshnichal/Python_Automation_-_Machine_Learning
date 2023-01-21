def main():
	user = int(input("Enter numbers: "))
	count = 0
	while user != 0:
		user //= 10
		count += 1
	print("Sum of Digits: ", count)


if __name__ == "__main__":
	main()


# def main():
# 	user = str(input("Enter numbers: "))
#
# 	print(len(user))
#
#
# if __name__ == "__main__":
# 	main()