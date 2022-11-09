
nums = ['1', 1234, "asbc", False, 564325]
# print(all(nums))


# nums = [False, None, 0, '', 1]
# print(any(nums))

# print(all([(1, 2, 3), []]))
# print(all([[], []]))
# print(all([]))


# print(any([(1, 2, 3), []]))

# print(any([]))		
# print(any([[], []]))

# data_collection_2 = [[True, False], [False, False], [True, True], 
#                      [10, 100, 1000], [0, 0, 0, 0], ['Python', 'C#'], 
#                      ['', '', 'language'], [(1, 2, 3), []], [], [[], []], 
#                      {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday'},
#                      {0: 'Monday'}, {'name': 'Timur', 'age': 28}, {'': 'None', 'age': 28}]
# for pair in data_collection_2:
# 	print(any(pair))

str1 = "del"
str2 = "delete ar"

if str1 in str2:
	print(True)