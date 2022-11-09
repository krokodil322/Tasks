nums = [set(item) for _ in range(2) for item in input().split()]
if nums[0].isdisjoint(nums[1]):
	print("NO")
else:
	print("YES")
