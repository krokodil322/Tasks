from math import factorial

# size = int(input())
# list1 = [[] * item for item in range(0, size)]
# print(list1)

# for index in range(0, size):
# 	if index < 2:
# 		list1[index] = 1
# 	else:
# 		if index % 2 == 0:
# 			list1[index].insert(0, 1)
# 			list1[index].insert(-1, 1)
# 			list1[index].insert(2, list1[index - 1][1] * 2)
# 			list1[index].insert(1, index)
# 		else:
# 			list1[index].insert(0, 1)
# 			list1[index].insert(-1, 1)
# 			list1[index].insert(1, index)
# 			list1[index].insert(1, index)
# 			# list1[index].insert(2, list1[index - 1][1] * 2)

# 	print(list1)
# row = [1]
# for x in zip([0]+row, row+[0]):
# 	print(sum(x))


nums = [1]
for cycle in range(int(input())):
    nums = [sum(x) for x in zip([0]+nums, nums+[0])]
print(nums) 

