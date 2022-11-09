point = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
input_data = list(input())
y = point.index(input_data[0])
x = int(input_data[1])
matrix = [['.' for _ in range(8)] for _ in range(8)]
matrix[8 - x][y] = 'N'

coef = 2
for shift in range(1, 3):
	if ((8 - x) - shift >= 0 and (8 - x) - shift <= 7) and (y + coef <= 7 and y + coef >= 0):
		matrix[(8 - x) - shift][y + coef] = '*'
	if ((8 - x) + shift >= 0 and (8 - x) + shift <= 7) and (y - coef <= 7 and y - coef >= 0):
		print((8 - x) + shift, y + coef, sep="|")
		matrix[(8 - x) + shift][y - coef] = "*"
	if ((8 - x) - shift >= 0 and (8 - x) - shift <= 7) and (y - coef <= 7 and y - coef >= 0):
		matrix[(8 - x) - shift][y - coef] = "*"
	if ((8 - x) + shift >= 0 and (8 - x) + shift <= 7) and (y + coef <= 7 and y + coef >= 0):
		print((8 - x) + shift, y + coef, sep="|")
		matrix[(8 - x) + shift][y + coef] = "*"
	coef -= 1

for item in matrix:
	for point in item:
		print(point, end="  ")
	print("\n")
