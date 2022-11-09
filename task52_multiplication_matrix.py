size1 = [int(item) for item in input().split()]
matrix1 = [[int(item) for item in input().split()] for _ in range(size1[0])]
input()
size2 = [int(item) for item in input().split()]
matrix2 = [[int(item) for item in input().split()] for _ in range(size2[0])]

def get_row_matrix1() -> list:
	for row in matrix1:
		yield row

def get_column_matrix2() -> list:
	for column in range(size2[1]):
		column_matrix2 = []
		for row in range(size2[0]):
			column_matrix2.append(matrix2[row][column])
		yield column_matrix2

multiplic_row_col, result = [], []
generator_row = get_row_matrix1()
for r in range(size1[0]):
	row_matrix1 = next(generator_row)
	generator_column = get_column_matrix2()
	for c in range(size2[1]):
		column_matrix2 = next(generator_column)
		total = 0
		for index in range(size2[0]):
			total += row_matrix1[index] * column_matrix2[index]
		multiplic_row_col.append(total)
	result.append(multiplic_row_col)
	multiplic_row_col = []

for item in result:
	for num in item:
		print(num, end=" ")
	print()
