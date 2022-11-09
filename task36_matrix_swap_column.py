row = int(input())
column = int(input())
matrix = [[int(item) for item in input().split()] for _ in range(row)]
swap_index = [int(item) for item in input().split()]
buffer_column = []
for c in range(column):
	for r in range(row):
		if swap_index[0] == c:
			buffer_column.append(matrix[r][swap_index[0]])
			matrix[r][swap_index[0]] = matrix[r][swap_index[1]]
			matrix[r][swap_index[1]] = buffer_column[r]
for item in matrix:
	for num in item:
		print(num, end=" ")
	print()