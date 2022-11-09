size = int(input())
matrix = [[0 for _ in range(size)] for _ in range(size)]

for r in range(size):
	matrix[r][size - r - 1] = 1
	matrix[r][r] = 1
for item in matrix:
	for num in item:
		print(num, end=" ")
	print()