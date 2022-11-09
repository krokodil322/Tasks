



slice_shift, slice_matrix= 1, []
for row in [[int(row) for row in input().split()] for _ in range(int(input()))]:
	slice_matrix.append(row[0:slice_shift:1])
	slice_shift += 1

max_value = slice_matrix[0][0]
for item in slice_matrix:
	if max(item) > max_value:
		max_value = max(item)
print(max_value)
