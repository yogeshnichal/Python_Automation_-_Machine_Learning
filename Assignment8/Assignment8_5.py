def factorial(No):
    if No == 1:
        return No
    else:
        return No*factorial(No-1)

Num = int(input("Enter number: "))
print("Factorial:", factorial(Num))

