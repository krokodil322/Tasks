
user_nums = [item for item in input().split()]
for index in range(0, len(user_nums) - 1, 2):
	user_nums[index], user_nums[index + 1] = user_nums[index + 1], user_nums[index]
print(" ".join(user_nums))



