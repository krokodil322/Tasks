


size = int(input())
matrix = [[int(item) for item in input().split()] for _ in range(size)]
result = [[] for _ in range(size * 2 - 1)]
numerals = [num for num in range(1, size + 1)]
buffer_numerals = numerals.copy()
status = True
for r in range(size):
	if status:
		buffer_numerals = numerals.copy()
		for c in range(size):
			if matrix[r][c] in buffer_numerals:
				# print(matrix[r][c])
				buffer_numerals.remove(matrix[r][c])
				# print(buffer_numerals)
			elif (matrix[r][c] not in buffer_numerals) and (len(buffer_numerals) != 0):
				status = False
		if len(buffer_numerals) != 0:
			status = False
			break 
	else:
		break
for c in range(size):
	if status:
		buffer_numerals = numerals.copy()
		for r in range(size):
			if matrix[r][c] in buffer_numerals:
				buffer_numerals.remove(matrix[r][c])
			elif matrix[r][c] not in buffer_numerals and len(buffer_numerals) != 0:
				status = False
		if len(buffer_numerals) != 0:
			status = False
			break 
	else:
		break
if status:
	print("YES")
else:
	print("NO")



