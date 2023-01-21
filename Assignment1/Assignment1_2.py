def chknum(value):
    formula = value
    return formula


def main():
    num = int(input("Enter any number: "))
    if num % 2 == 0:
        print("Even Number")
    else:
        print("Odd Number")

    fix = chknum(num)


if __name__ == "__main__":
    main()
