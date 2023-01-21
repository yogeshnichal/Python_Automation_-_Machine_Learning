def arithmetic(num1, op, num2):
	if op == "+":
		print(num1 + num2)
	elif op == "-":
		print(num1 - num2)
	elif op == "*":
		print(num1 * num2)
	elif op == "/":
		print(num1 / num2)


def main():
	num1 = int(input("Enter first number: "))
	arth = input("Enter Operator: ")
	num2 = int(input("Enter second number: "))

	total = arithmetic(num1,arth,num2)


if __name__ == "__main__":
	main()