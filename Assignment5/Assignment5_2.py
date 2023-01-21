class Circle:
	PI = 3.14
	def __init__(self):
		self.R = 0.0
		self.A = 0.0
		self.C = 0.0
	def Accept(self):
		self.R = float(input("Enter Radius Value: "))
	def CalculateArea(self):
		self.A = self.PI * self.R ** 2
	def CalculateCircumference(self):
		self.C = self.PI * self.R * 2
	def Display(self):
		print("Area is: {0}\nCircumference is:{1}".format(self.A, self.C))


def main():
	obj1 = Circle()

	obj1.Accept()
	obj1.CalculateArea()
	obj1.CalculateCircumference()
	obj1.Display()


if __name__ == "__main__":
	main()
