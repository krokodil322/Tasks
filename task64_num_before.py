numbers = [int(item) for item in input().split()]
before_numbers = set()

for item in numbers:
	if item not in before_numbers:
		print("NO")
		before_numbers.add(item)
	else:
		print("YES")