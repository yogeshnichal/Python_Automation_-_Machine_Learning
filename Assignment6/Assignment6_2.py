# Class Name as BankAccount
# Instance Variables as Name, Amount
# Class Variable as ROI
# Instance Methods as Display(), Deposit(), Withdraw(), CalculateInterest()

class BankAccount:
	ROI = 10.5

	def __init__(self):
		self.Name = input("Name Your: ")
		self.Amount = 0

	def Deposit(self):
		value = int(input("Enter Deposit Amount: "))
		self.Amount = self.Amount + value

	def Withdraw(self):
		value = int(input("Enter Withdraw Amount: "))
		self.Amount = self.Amount - value

	def CalculateIntrest(self):
		time = int(input("Years: "))
		print("Your Amount ROI is:", self.Amount * time * BankAccount.ROI / 100)

	def Display(self):
		print("Name is: {}\nYour Ac. Amount is: {}".format(self.Name, self.Amount))


def main():
	Obj = BankAccount()
	Obj.Deposit()
	Obj.Withdraw()
	Obj.Display()
	Obj.CalculateIntrest()



if __name__ == "__main__":
	main()
