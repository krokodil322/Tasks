
# matrix = [[int(num) for num in item] for item in input().split()]
# print(matrix)
N = int(input())
matrix = [[0] * N] * N

j = 0
for row in range(N):
	for item in input().split():
		matrix[j].append(item)
		j += 1

print(matrix)