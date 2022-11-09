point = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
SIZE = 8

input_data = list(input())
x, y = int(input_data[1]), point.index(input_data[0])

matrix = [['.' for _ in range(8)] for _ in range(8)]
for c in range(SIZE):
	matrix[-x][c] = "*"
for r in range(SIZE):
	matrix[r][y] = "*"

for i in range(SIZE * 2 - 1):
    for j in range(SIZE):
        if ((i-j) > -1) and ((i-j) < SIZE) and i == (SIZE - x) + (SIZE - y) - 1:
            matrix[j][j - i - 1] = "*"
for i in range(SIZE * 2 - 1):
    for j in range(SIZE):
        if ((i-j) > -1) and ((i-j) < SIZE) and i == (SIZE - x) + (y - 1) + 1:
            matrix[j][i - j] = "*"

matrix[8 - x][y] = 'Q'

for item in matrix:
	for point in item:
		print(point, end=" ")
	print()
