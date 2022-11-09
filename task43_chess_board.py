size = [int(item) for item in input().split()]
matrix = [['.' for _ in range(size[1])] for _ in range(size[0])]

for i in range(size[0]):
	for j in range(size[1]):
		if (i + 1) % 2 != 0 and (j + 1) % 2 == 0:
			matrix[i][j] = "*"
		elif (i + 1) % 2 == 0 and (j + 1) % 2 != 0:
			matrix[i][j] = "*"
for item in matrix:
	for char in item:
		print(char, end=" ")
	print()