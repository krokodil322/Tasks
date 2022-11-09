
row = int(input())
column = int(input())

matrix = [[int(item) for item in input().split()] for _ in range(row)]
row_max_num, column_max_num, max_num = 0, 0, matrix[0][0]
for r in range(row):
	for c in range(column):
		if matrix[r][c] > max_num:
			max_num = matrix[r][c]
			row_max_num, column_max_num = r, c
print(row_max_num, column_max_num, sep=" ")