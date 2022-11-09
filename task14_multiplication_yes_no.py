# from itertools import combinations

# numbers = [input() for cycle in range(0, int(input()))]
# combinations = list(combinations(numbers, 2))
# print(combinations)
# multiplication = [int(item[0]) * int(item[1]) for item in list(combinations(numbers, 2))]
# print(multiplication)
# if int(input()) in [int(item[0]) * int(item[1]) for item in list(combinations(numbers, 2))]:
# 	print("ДА")
# else:
# 	print("НЕТ")
# print(multiplication)

from itertools import combinations
numbers = [input() for cycle in range(0, int(input()))]
if int(input()) in [int(item[0]) * int(item[1]) for item in list(combinations(numbers, 2))]:
	print("ДА")
else:
	print("НЕТ")