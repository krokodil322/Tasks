nums = [set(item) for _ in range(int(input())) for item in input().split()]
result = set(nums[0])
for item in nums:
	result = result.intersection(item)
print(*result)