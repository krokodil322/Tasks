size = [int(item) for item in input().split()]
matrix = [[0 for _ in range(size[1])] for _ in range(size[0])]

value_sequence = 1
for c in range(size[1]):
	for r in range(size[0]):
		matrix[r][c] = value_sequence
		value_sequence += 1

for row_index in range(size[0]):
	for column_index in range(size[1]):
		print(str(matrix[row_index][column_index]).ljust(3), end=" ")
	print()