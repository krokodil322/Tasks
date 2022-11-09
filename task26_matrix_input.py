

i = int(input())
j = int(input())
matrix = [[0 for _ in range(j)] for _ in range(i)]
for row_index in range(i):
	for column_index in range(j):
		matrix[row_index][column_index] = input()
for row_index in range(i):
	for column_index in range(j):
		print(matrix[row_index][column_index], end=' ', sep=" ")
	print()
