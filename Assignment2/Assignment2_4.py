def main():
	user = int(input("Enter number: "))
	fact = 1
	total = 0
	while fact < user:
		if user % fact == 0:
			total += fact
			print(fact)
		fact += 1

	print("Factor:", total)


if __name__ == "__main__":
	main()
