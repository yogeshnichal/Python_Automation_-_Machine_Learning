def Summation(No):
    if len(No) == 0:
        return 0
    return No[0] + Summation(No[1:])


lst = [int(input("1: ")), int(input("2: ")), int(input("3: "))]

print("Total:", Summation(lst))

# def Summation(No):
#     if len(No) == 0:
#         return 0
#     return No[0] + Summation(No[1:])
#
# lst = []
# iSize = int(input("Enter length of list: "))
# for i in range(iSize):
#     num = int(input("Enter numbers: "))
#     lst.append(num)
#
# print("Total:", Summation(lst))
