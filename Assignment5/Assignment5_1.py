class Demo:
    def __init__(self, value1, value2):
        self.No1 = value1
        self.No2 = value2

    value = input("Enter anything: ")

    def Fun(self):
        print("Fun:", self.No1, self.No2)

    def Gun(self):
        print("Gun:", self.No1, self.No2)


def main():
    obj1 = Demo(11, 21)
    obj2 = Demo(51, 101)

    obj1.Fun()
    obj2.Fun()
    obj1.Gun()
    obj2.Gun()


if __name__ == "__main__":
    main()