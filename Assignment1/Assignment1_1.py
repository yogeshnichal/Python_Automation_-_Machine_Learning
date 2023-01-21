def fun(word):
    formula = word
    return formula


def main():
    out = "Hello from Fun"
    var = input("Say Hi:")
    if var == "hi":
        print(out)
    else:
        print("bye..")

    fix = fun(out)


if __name__ == "__main__":
    main()
