nums = [set([int(item) for item in input().split()]) for _ in range(3)]
intersections = list()
intersections.append(nums[0].symmetric_difference(nums[1]))
intersections.append(nums[1].symmetric_difference(nums[2]))
intersections.append(nums[0].symmetric_difference(nums[2]))
nums = set(intersections[0])
for item in intersections:
	nums.update(item)

# print(intersections)

print(nums)