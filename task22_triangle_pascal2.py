nums = [1]
for cycle in range(int(input())):
	for item in nums:
		print(item, end=" ")
	print()
	nums = [sum(x) for x in zip([0]+nums, nums+[0])]
