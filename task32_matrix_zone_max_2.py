from math import ceil

size = int(input())
matrix = [[int(row) for row in input().split()] for _ in range(size)]
slice_values = []
#ЛЕВЫЙ СТОЛБЕЦ
for i in range(size):
	for j in range(1):
		slice_values.append(matrix[i][j])
#ПРАВЫЙ СТОЛБЕЦ
for i in range(size-1, -1, -1):
	for j in range(1):
		slice_values.append(matrix[i][-1])
#ГЛАВНАЯ ДИАГОНАЛЬ
for i in range(size):
	slice_values.append(matrix[i][i])
#ПОБОЧНАЯ ДИАГОНАЛЬ
for i in range(size):
	slice_values.append(matrix[i][size - i - 1])
#СРЕДИННЫЕ СТРОКИ(ГОРИЗОНТ)
if size % 2 == 0:
	i = int(ceil(size / 2) - 1)
	for cycle in range(size):
		for j in range(size):
			slice_values.append(matrix[i][j])
		if i > ((size / 2) - 1):
			break
		i += 1
else:
	i = int(size / 2) 
	for j in range(size):
		slice_values.append(matrix[i][j])
print(max(slice_values))
	
	

