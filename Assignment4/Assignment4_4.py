from functools import reduce
CheckEven = lambda Num: Num % 2 == 0

Square = lambda Num: Num ** 2

Sum = lambda A, B: A + B

def main():
	lst = []
	iSize = int(input("Enter size of list: "))

	for i in range(0, iSize, 1):
		Value = int(input("Enter value: "))
		lst.append(Value)

	print("User List:", lst)

	Data_Filter = list(filter(CheckEven, lst))
	print("FilterX:", Data_Filter)

	Data_Map = list(map(Square, Data_Filter))
	print("MapX:", Data_Map)

	Data_Reduce = reduce(Sum, Data_Map)
	print("ReduceX:", Data_Reduce)


if __name__ == "__main__":
	main()
