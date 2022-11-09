nums = [set([int(item) for item in input().split()]) for _ in range(3)]
student3 = nums[2]
for index in range(len(nums) - 1):
	student3.difference_update(nums[index])
print(*sorted(student3, reverse=True))
