from functools import reduce
CheckNum = lambda No: No >= 70 and No <= 90

AddNum = lambda No: No + 10

MultiNum = lambda A,B: A * B

def main():
	lst = []
	iSize = int(input("Enter size of list: "))

	for iCnt in range(0, iSize, 1):
		value = int(input("Enter value: "))
		lst.append(value)

	print("Input list:", lst)

	Data_Filter = list(filter(CheckNum, lst))
	print("Filter Data:", Data_Filter)

	Data_Map = list(map(AddNum, Data_Filter))
	print("Map Data:", Data_Map)

	Data_Reduce = reduce(MultiNum, Data_Map)

	print("Reduce Data:", lambda MultiNum, Data_Map: MultiNum * Data_Map, Data_Reduce)


if __name__ == "__main__":
	main()
