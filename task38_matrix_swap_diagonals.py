size = int(input())
matrix = [[int(item) for item in input().split()] for _ in range(size)]

diagonals = [[], []]
for i in range(size):
	diagonals[0].append(matrix[i][i])
	diagonals[1].append(matrix[i][size - i - 1])
for i in range(size):
	matrix[i][i] = list(reversed(diagonals[1]))[i]
	matrix[i][size - i - 1] = list(reversed(diagonals[0]))[i]
for item in matrix:
	for num in item:
		print(num, end=" ")
	print()