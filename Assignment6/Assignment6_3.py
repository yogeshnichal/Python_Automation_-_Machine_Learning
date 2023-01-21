# Class as Arithmetic
# Instance Variable as Value
# Instance Methods as ChkPrime(), ChkPerfect(), SumFactors(), Factors()

class Arithmetic:
    def __init__(self, Value):
        self.Value = Value

    def ChkPrime(self):
        num = self.Value
        iCnt = 0
        i = 1

        while i <= num:
            if num % i == 0:
                iCnt += 1
            i += 1
        if iCnt == 2:
            print("Number is Prime:", True)
        else:
            print("Number is Prime:", False)

    def ChkPerfect(self):
        num = self.Value
        Sum = 0
        for i in range(1, num):
            if num % i == 0:
                Sum += i
        if Sum == num:
            print("Number is Perfect:", True)
        else:
            print("Number is Perfect:", False)

    def SumFactors(self):
        num = self.Value
        Sum = 0
        for i in range(1, num):
            if num % i == 0:
                Sum += i
        print("Sum of factors is: {0}".format(Sum))

    def Factors(self):
        num = self.Value
        lst = []

        for i in range(1, num + 1):
            if num % i == 0:
                lst.append(i)
        print("Factors are: {}".format(lst[:-1]))


def main():
    num = int(input("Enter any number: "))
    Obj = Arithmetic(num)

    Obj.ChkPrime()
    Obj.ChkPerfect()
    Obj.SumFactors()
    Obj.Factors()


if __name__ == "__main__":
    main()