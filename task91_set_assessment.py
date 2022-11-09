nums = [set([int(item) for item in input().split()]) for _ in range(3)]
print( *sorted( nums[0].intersection(nums[1]).difference(nums[2]), reverse=True ) )