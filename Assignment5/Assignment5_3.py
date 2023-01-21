class Arithmatic:
	def __init__(self):
		self.value1 = 0.0
		self.value2 = 0.0
	def Accept(self):
		self.value1 = float(input("Enter Value1: "))
		self.value2 = float(input("Enter Value2: "))
	def Addition(self):
		print("Addition is:", self.value1 + self.value2)
	def Subtraction(self):
		print("Subtraction is:", self.value1 - self.value2)
	def Multiplication(self):
		print("Multiplication is:", self.value1 * self.value2)
	def Division(self):
		print("Division is:", self.value1 / self.value2)


def main():
	obj1 = Arithmatic()

	obj1.Accept()
	obj1.Addition()
	obj1.Subtraction()
	obj1.Multiplication()
	obj1.Division()


if __name__ == "__main__":
	main()
