size = int(input())
matrix = [[int(item) for item in input().split()] for _ in range(size)]
power = int(input())
base_matrix = matrix.copy()
def get_row_matrix1() -> list:
	for row in matrix:
		yield row

def get_column_matrix2() -> list:
	for column in range(size):
		column_matrix = []
		for row in range(size):
			column_matrix.append(base_matrix[row][column])
		yield column_matrix

counter = 0
for _ in range(power - 1):
	if counter >= 1:
		matrix = result.copy()
	multiplic_row_col, result = [], []
	generator_row = get_row_matrix1()
	for r in range(size):
		row_matrix = next(generator_row)
		# print(f"row_matrix: {row_matrix}, counter: {counter}")
		generator_column = get_column_matrix2()
		for c in range(size):
			column_matrix2 = next(generator_column)
			# print(f"\tcolumn_matrix: {column_matrix2}")
			total = 0
			for index in range(size):
				total += row_matrix[index] * column_matrix2[index]
				# print(f"\t\ttotal:{total}, index:{index}")
			multiplic_row_col.append(total)
		result.append(multiplic_row_col)
		multiplic_row_col = []
	counter += 1

for item in result:
	for num in item:
		print(num, end=" ")
	print()
