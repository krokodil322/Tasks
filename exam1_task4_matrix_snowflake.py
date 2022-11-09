from math import floor
size = int(input())
matrix = [['.' for _ in range(size)] for _ in range(size)]
for r in range(size):
	matrix[r][r] = "*"
	matrix[r][size - r - 1] = "*"
	matrix[r][floor(size/2)] = "*"
	matrix[floor(size/2)][r] = "*"
for item in matrix:
	for num in item:
		print(num, end=" ")
	print()