user_nums = [int(num) for num in input().split()]
before, count = user_nums[0], 1
for num in user_nums:
	if num > before:
		count += 1
	before = num
print(count)