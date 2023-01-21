# Return Addition of Two Numbers

def add(value1, value2):
	formula = value1 + value2
	return formula


def main():
	num1 = float(input("Enter first number: "))
	num2 = float(input("Enter second number: "))

	fix = add(num1, num2)
	print("Addition of Two Numbers:", fix)


if __name__ == "__main__":
	main()
