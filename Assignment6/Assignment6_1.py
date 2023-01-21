# Class Name as BookStore
# Instance Variables as Name, Author
# Class Variable as NoOfBooks
# Instance Methods as Display()

class BookStore:
	NoOfBooks = 0

	def __init__(self, Name, Author):
		self.Name = Name
		self.Author = Author
		BookStore.NoOfBooks += 1

	def Display(self):
		print("{} by {}. No of Books: {}".format(self.Name, self.Author, BookStore.NoOfBooks))


def main():
	Obj1 = BookStore(input("Enter Book Name: "), input("Enter Author Name: "))
	Obj1.Display()

	Obj2 = BookStore(input("Enter Book Name: "), input("Enter Author Name: "))
	Obj2.Display()


if __name__ == "__main__":
	main()