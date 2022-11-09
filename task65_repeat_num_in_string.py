nums = [set([int(item) for item in input().split()]) for _ in range(2)]
# print(sum([1 for item in nums[0] for item2 in nums[1] if item == item2]))
print(len(nums[1].intersection(nums[0])))