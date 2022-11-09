nums = [set(item) for _ in range(2) for item in input().split()]
# print("YES" if nums[0].issubset(nums[1]) else "NO")
print("YES" if nums[1].issubset(nums[0]) else "NO")