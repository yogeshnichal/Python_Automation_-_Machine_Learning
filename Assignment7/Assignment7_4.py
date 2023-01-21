
import threading


def small(String):
	lst = []
	num = String
	for i in num:
		if i.islower():
			lst.append(i)
	print("small list: {}\nsmall length: {}\nsmall id: {}".format(lst, len(lst), id(small)))

def capital(String):
	lst = []
	num = String
	for i in num:
		if i.isupper():
			lst.append(i)
	print("capital list: {}\ncapital length: {}\ncapital id: {}".format(lst, len(lst), id(capital)))

def digits(String):
	lst = []
	num = String
	for i in num:
		if i.isdigit():
			lst.append(i)
	print("digits list: {}\ndigits length: {}\ndigits id: {}".format(lst, len(lst), id(digits)))


def main():
	String = input("Enter Value: ")

	T1 = threading.Thread(target=small, args=(String,))
	T2 = threading.Thread(target=capital, args=(String,))
	T3 = threading.Thread(target=digits, args=(String,))

	T1.start()
	T2.start()
	T3.start()

	T1.join()
	T2.join()
	T3.join()


if __name__ == "__main__":
	main()



# import threading
#
# def small(String):
# 	lst = [i for i in String if i.islower()]
# 	print("small list: {}\nsmall length: {}\nsmall id: {}".format(lst, len(lst), id(small)))
#
#
# def capital(String):
# 	lst = [i for i in String if i.isupper()]
# 	print("capital list: {}\ncapital length: {}\ncapital id: {}".format(lst, len(lst), id(capital)))
#
#
# def digits(String):
# 	lst = [i for i in String if i.isdigit()]
# 	print("digits list: {}\ndigits length: {}\ndigits id: {}".format(lst, len(lst), id(digits)))
#
# def main():
# 	String = input("Enter Value: ")
#
#
# 	T1 = threading.Thread(target=small, args=(String,))
# 	T2 = threading.Thread(target=capital, args=(String,))
# 	T3 = threading.Thread(target=digits, args=(String,))
#
# 	T1.start()
# 	T2.start()
# 	T3.start()
#
# 	T1.join()
# 	T2.join()
# 	T3.join()
#
#
# if __name__ == "__main__":
# 	main()

