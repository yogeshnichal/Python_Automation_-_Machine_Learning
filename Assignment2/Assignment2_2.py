def main():
	star = int(input("Enter number: "))
	for i in range(star):
		for X in range(star):
			print("*", end="  ")
		print()


if __name__ == "__main__":
	main()