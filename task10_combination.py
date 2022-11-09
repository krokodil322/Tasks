
# РАБОТАЕТ!
# import itertools
# print(sum([1 for values in list(itertools.pairwise(input().split())) if values[1] > values[0]]))



# count_more_previous, previos_num = 0, user_nums[0]
# for num in user_nums:
# 	if num > previos_num:
# 		count_more_previous += 1
# 	previos_num = num

user_nums = [int(item) for item in input().split()]
print(sum([1 for index in range(1, len(user_nums)) if user_nums[index] > user_nums[index - 1]]))

# print(count_more_previous)

