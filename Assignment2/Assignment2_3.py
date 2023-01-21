# Factorial from user input

def main():
	user = int(input("Enter Number: "))
	fact = 1
	while user > 0:
		fact *= user
		user -= 1
	print("Factorial:", fact)


if __name__ == "__main__":
	main()
