nums = [set([int(item) for item in input().split()]) for _ in range(2)]
print(*sorted(nums[0].intersection(nums[1])))