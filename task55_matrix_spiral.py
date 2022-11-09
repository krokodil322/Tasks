size = [int(item) for item in input().split()]
matrix = [[0 for _ in range(size[1])] for _ in range(size[0])]

def check_full_matrix() -> bool:
	for item in matrix:
		for num in item:
			if num == 0:
				return True
	return False

sequence = 1
start_col, end_col = 0, size[1]
start_row, end_row = 0, size[0]
counter = 0
while (counter != size[1]) and (counter != size[0]):
	if check_full_matrix():
		for c in range(start_col, end_col):
			matrix[start_row][c] = sequence
			sequence += 1
	else:
		break
	start_row += 1
	if check_full_matrix():
		for r in range(start_row, end_row):
			print(sequence)
			matrix[r][end_col - 1] = sequence
			sequence += 1
	else:
		break
	end_col -= 1
	if check_full_matrix():
		for c in range(end_col - 1, start_col - 1, -1):
			matrix[end_row - 1][c] = sequence  
			sequence += 1
	else:
		break
	end_row -= 1
	if check_full_matrix():
		for r in range(end_row - 1, start_row - 1, -1):
			matrix[r][start_col] = sequence  
			sequence += 1
	else:
		break
	start_col += 1
	counter += 1
	
for row_index in range(len(matrix)):
    for column_index in range(len(matrix[0])):
        print(str(matrix[row_index][column_index]).ljust(3), end=" ")
    print()