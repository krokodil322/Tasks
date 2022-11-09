

quan = int(input())
# [print([num for num in range(1, quan + 1)]) for item in range(1, quan + 1)]
# 6
# ВЫВОД
# [1, 2, 3, 4, 5, 6]
# [1, 2, 3, 4, 5, 6]
# [1, 2, 3, 4, 5, 6]
# [1, 2, 3, 4, 5, 6]
# [1, 2, 3, 4, 5, 6]
# [1, 2, 3, 4, 5, 6]

# list1 = []
# for item in range(1, quan + 1):
# 	for num in range(1, item + 1):
# 		list1.append(num)
# 	print(list1)
# 	list1 = []

[print([num for num in range(1, item + 1)]) for item in range(1, quan + 1)]
