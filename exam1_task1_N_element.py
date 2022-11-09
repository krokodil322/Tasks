
list_chars = [char for char in input().split()]
N = int(input())
result = [[] for _ in range(N)]

for cycle in range(N):
	counter = 0
	for index in range(1, len(list_chars) + 1):
		if (counter == 0) or counter % N == 0:
			result[cycle].append(list_chars[index - 1])
		counter += 1
	list_chars.pop(0)

print(result)