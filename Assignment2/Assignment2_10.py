def main():
	user = int(input("Enter numbers: "))
	total = 0

	while user > 0:
		total += user % 10
		user //= 10
	print("Sum of Digits: ", total)


if __name__ == "__main__":
	main()
