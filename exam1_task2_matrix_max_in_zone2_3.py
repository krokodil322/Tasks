

result, shift = [], 2
for row in [[int(item) for item in input().split()] for _ in range(int(input()))]:
	result.append(row[-1:-shift:-1])
	shift += 1
print(max([num for item in result for num in item]))