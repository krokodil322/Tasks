size = int(input())
matrix = [['.' for _ in range(size)] for _ in range(size)]

sequence, reverse = size, True
for i in range(size * 2 - 1):
	for j in range(size):
		if ((i - j) > -1) and ((i - j) < size):
			matrix[j][j - i] = sequence
	if reverse:
		sequence-=1
	else:
		sequence+=1
	if sequence == -1:
		reverse = False
		sequence += 2

slice_column = []

for r in range(size):
	slice_column.append(matrix[r][0] - 1)
slice_column = list(reversed(slice_column))
for r in range(size):
	matrix[r][0] = slice_column[r]

for row_index in range(len(matrix)):
    for column_index in range(len(matrix[0])):
        print(str(matrix[row_index][column_index]).ljust(3), end=" ")
    print()