

counter, middle = 0, 0
for row in [[int(row) for row in input().split()] for _ in range(int(input()))]:
	middle = sum(row) / len(row)
	for num in row:
		if num > middle:
			counter += 1
	print(counter)
	counter = 0
counter = sum([1 for num in row if num > middle])

#БОЛЕЕ КРАТКАЯ ВЕРСИЯ, РАБОТАЕТ!
# for row in [[int(row) for row in input().split()] for _ in range(int(input()))]:
# 	counter = sum([1 for num in row if num > sum(row) / len(row)])
# 	print(counter)
# 	counter = 0