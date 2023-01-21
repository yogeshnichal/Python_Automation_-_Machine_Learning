def Pattern(No):
	if No > 1:
		Pattern(No-1)
	print(No, end=' ')

Pattern(5)