size = [item for item in input().split()]
size = [int(num) for num in size]
matrix = [[0 for _ in range(size[1])] for _ in range(size[0])]

base_row = [i + 1 for i in range(size[1])]
for r in range(size[0]):
	for c in range(size[1]):
		for num in base_row:
			matrix[r][c] = base_row[c]
			break
shift, index = 0, 1
if size[0] > size[1]:
	iterator = size[0]
else:
	iterator = size[1]
for _ in range(iterator):
	slice_matrix = matrix[shift][1:size[1] - shift:1]
	print(index, size[0], shift, sep="|")
	if index <= size[0] - 1:
		for num in slice_matrix:
			for item in matrix[index]:
				if num == item:
					matrix[index].remove(num)
		slice_matrix = list(reversed(slice_matrix))
		for num in slice_matrix:
			matrix[index].insert(0, num)
		shift += 1
		if matrix[index] == base_row:
			shift = 0
		index += 1

for item in matrix:
	for num in item:
		print(num, end=" ")
	print()
	