size = int(input())
matrix = [[int(item) for item in input().split()] for _ in range(size)]
mirror_matrix = []
mirror_matrix = [[matrix[j][i] for j in range(size)] for i in range(size)]
mirror_matrix = [[mirror_matrix[i][j] for j in range(size)] for i in range(size)]
mirror_matrix = [list(reversed(item)) for item in mirror_matrix]
mirror_matrix = [[mirror_matrix[j][i] for j in range(size)] for i in range(size)]
matrix = [[mirror_matrix[j][i] for j in range(size)] for i in range(size)]
for item in matrix:
	for num in item:
		print(num, end=" ")
	print()