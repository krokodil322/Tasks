size = int(input())
matrix = [[0 for _ in range(size)] for _ in range(size)]

for i in range(size):
	matrix[i][size - i - 1] = 1
	for j in range(size):
		if i >= size / 2:
			matrix[i][i] = 2
		if (i < j and size > i + j + 1) or (i > j and size > i + j + 1):
			matrix[i][j] = 0
		if (i < j and size < i + j + 1) or (i > j and size < i + j + 1):
			matrix[i][j] = 2
			
for item in matrix:
	for char in item:
		print(char, end=" ")
	print()