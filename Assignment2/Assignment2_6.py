def main():
	user = int(input("Enter number : "))
	star = ' * '
	while 1 <= user:
		print(star * user)
		user -= 1


if __name__ == "__main__":
	main()
