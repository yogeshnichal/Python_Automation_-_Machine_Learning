def Pattern(No):
	print(No, end=' ')
	if No == 1:
		return 0
	return Pattern(No - 1)

Pattern(5)
