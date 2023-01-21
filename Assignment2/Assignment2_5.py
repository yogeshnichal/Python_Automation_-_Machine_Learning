def main():
	user = int(input("Enter number: "))
	count = 0
	i = 1
	while i <= user:
		if user % i == 0:
			count += 1
		i += 1
	if count == 2:
		print("Prime Number: ")
	else:
		print("Not Prime")


if __name__ == "__main__":
	main()
