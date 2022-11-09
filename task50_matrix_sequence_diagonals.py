size = [item for item in input().split()]
size = [int(num) for num in size]
matrix = [[0 for _ in range(size[1])] for _ in range(size[0])]

# for i in range(size[0]):
# 	for j in range(size[1]):
# 		matrix[i][j] =


sequence = 1


counter, index_c, index_r = 1, 0, 0
for r in range(size[0]):
	for row_index in range(len(matrix)):
		for column_index in range(len(matrix[0])):
			print(str(matrix[row_index][column_index]).ljust(3), end=" ")
		print()
	print()
	for c in range(size[1]):
		matrix[r][c] = sequence
		sequence += 1

def column_up_plus(r: int=0, c: int=0) -> list:
	"""УВЕЛИЧИВАЕТ ИНДЕКС КОЛОНКИ"""
	"""ВОЗВРАЩАЕТ СПИСОК С ПАРОЙ КООРДИНАТ"""
	c += 1
	return [r, c]

def row_up_plus(r: int=0, c:int=0) -> list:
	"""УВЕЛИЧИВАЕТ ИНДЕКС СТРОКИ"""
	"""ВОЗВРАЩАЕТ СПИСОК С ПАРОЙ КООРДИНАТ"""
	r += 1
	return [r, c]

def column_down_minus(r: int=0, c:int=0) -> list:
	"""УМЕНЬШАЕТ ИНДЕКС КОЛОНКИ"""
	"""ВОЗВРАЩАЕТ СПИСОК С ПАРОЙ КООРДИНАТ"""
	c -= 1
	return [r, c]

def row_down_minus(r: int=0, c:int=0) -> list:
	"""УМЕНЬШАЕТ ИНДЕКС СТРОКИ"""
	"""ВОЗВРАЩАЕТ СПИСОК С ПАРОЙ КООРДИНАТ"""
	r -= 1
	return [r, c]



# for row_index in range(len(matrix)):
# 	for column_index in range(len(matrix[0])):
# 		print(str(matrix[row_index][column_index]).ljust(3), end=" ")
# 	print()
# 00 10 20 30 40
# 01 11 21 31 41
# 02 12 22 32 42
# 03 13 23 33 43
# 04 14 24 34 44

#индексы
# 11 12 13 14 15
# 21 22 23 24 25
# 31 32 33 34 35
# 41 42 43 44 45
# 51 52 53 54 55

#диагональное 
# заполнение
# 10 11 13 16 20
# 12 14 17 21 25
# 15 18 22 26 29
# 19 23 27 30 32
# 24 28 31 33 34

# 00
# 01 10
# 02 11 20
# 03 12 21 30