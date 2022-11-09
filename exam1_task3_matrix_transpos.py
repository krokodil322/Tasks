matrix = [[int(item) for item in input().split()] for _ in range(int(input()))]
result = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix[0]))]

for r in range(len(matrix[0])):
	for c in range(len(matrix[0])):
		result[c][r] = matrix[r][c]
for item in result:
	for num in item:
		print(num, end=" ")
	print()