from itertools import permutations

def get_biggest(nums: list) -> int:
	if len(nums) == 0:
		return -1
	transform = lambda pack: "".join([str(num) for num in pack])
	return max(map(transform, permutations(nums, len(nums))))



print(get_biggest([1, 2, 3]))
print(get_biggest([61, 228, 9, 3, 11]))
print(get_biggest([7, 71, 72]))
# print(get_biggest([13, 221, 423, 53, 1, 2, 33, 58, 78554, 34, 65, 65, 2, 1])) #78554656558534233433222211311