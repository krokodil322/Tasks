size = [int(item) for item in input().split()]
matrix1 = [[int(item) for item in input().split()] for _ in range(size[0])]
input()
matrix2 = [[int(item) for item in input().split()] for _ in range(size[0])]
result = [[0 for _ in range(size[1])] for _ in range(size[0])]
for r in range(size[0]):
	for c in range(size[1]):
		result[r][c] = matrix1[r][c] + matrix2[r][c]
for item in result:
	for num in item:
		print(num, end=" ")
	print()


