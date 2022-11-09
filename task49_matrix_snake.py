size = [item for item in input().split()]
size = [int(num) for num in size]
matrix = [[0 for _ in range(size[1])] for _ in range(size[0])]
#size[0] - кол-во строка
#size[1] - кол-во столбцов

reverse = False
sequence = 1
column_index = -1
for r in range(size[0]):
	for c in range(size[1]):
		if reverse is False:
			column_index += 1
		elif reverse is True:
			column_index -= 1
		matrix[r][column_index] = sequence
		sequence += 1
	if reverse is False:
		reverse = True
		column_index = 0
	elif reverse is True:
		reverse = False
		column_index = -1
		
for row_index in range(len(matrix)):
	for column_index in range(len(matrix[0])):
		print(str(matrix[row_index][column_index]).ljust(3), end=" ")
	print()

