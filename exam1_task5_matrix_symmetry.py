size = int(input())
matrix = [[int(item) for item in input().split()] for _ in range(size)]
result = [[] for _ in range(size * 2 - 1)]

for i in range(size * 2 - 1):
    for j in range(size):
        if ((i-j) > -1) and ((i-j) < size):
            result[i].append(matrix[j][i-j])
status = True
for index in range(round(len(result)/2)):
	if result[index] != result[-index-1]:
		print("NO")
		status = False
		break
if status:
	print("YES")



