point = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
input_data = list(input())
y = point.index(input_data[0])
x = int(input_data[1])
matrix = [['.' for _ in range(8)] for _ in range(8)]

print(x, y)

for c in range(8):
	matrix[-x][c] = "*"
for r in range(8):
	matrix[r][y] = "*"

for i in range(8 * 2 - 1):
    for j in range(8):
        if ((i-j) > -1) and ((i-j) < 8) and i == abs((8 - x) + (8 - y)) - 1:
            matrix[j][j - i - 1] = "*"

#===========================================================================================
for i in range(8 * 2 - 1):
    for j in range(8):
        if ((i-j) > -1) and ((i-j) < 8) and i == (8 - x) + (y - 1) + 1:
            matrix[j][i - j] = "*"

matrix[8 - x][y] = 'Q'

for item in matrix:
	for point in item:
		print(point, end="   ")
	print("\n")