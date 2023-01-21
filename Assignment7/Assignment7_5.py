
import threading

def thread1(No):
    if No > 0:
        No -= 1
        thread1(No)
        print(No+1)

def thread2(No):
    if No > 0:
        print(No)
        No -= 1
        thread2(No)


def main():
    Num = 50

    T1 = threading.Thread(target=thread1, args=(Num,))
    T2 = threading.Thread(target=thread2, args=(Num,))

    T1.start()
    T1.join()

    T2.start()


if __name__ == "__main__":
    main()



# import threading
#
# def thread1(No):
#     for i in range(No):
#         print(i)
#
# def thread2(No):
#     for i in range(No, -1, -1):
#         print(i)
#
# def main():
#     Num = 50
#
#     T1 = threading.Thread(target=thread1, args=(Num,))
#     T2 = threading.Thread(target=thread2, args=(Num,))
#
#     T1.start()
#     T1.join()
#
#     T2.start()
#
#
# if __name__ == "__main__":
#     main()