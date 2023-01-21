def main():
	user = int(input("Enter number: "))

	for i in range(1, user+1):
		for x in range(1, i+1):
			print(x, end="  ")
		print()


if __name__ == "__main__":
	main()
