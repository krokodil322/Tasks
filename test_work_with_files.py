
# with open("TEST_DATA.txt", encoding="utf-8") as torrent:
# 	result = list(map(str, torrent.readlines()))
# 	print(result)
		
# with open(input(), 'r', encoding="utf-8") as torrent:
#     result = list(map(str.strip, torrent.readlines()))
#     print(result[-2])

# from random import choice
# with open(input(), encoding="utf-8") as torrent:
# 	print(choice(list(torrent)))


# with open("TEST_DATA.txt", encoding="utf-8") as torrent:
# 	# print(sum(map(int, filter(lambda item: True if item != "" else False, map(str.strip, torrent.readlines())))))
# 	print(sum(map(int, torrent.read().split())))
	
    # print(sum(list(map(int, map(str.strip, torrent.readlines())))))
# from functools import reduce
# with open("TEST_DATA.txt", encoding="utf-8") as torrent:
# 	filtred = [item.split()[1:] for item in "".join(torrent).split('\n')]
# 	filtred = filter(lambda item: any(item), price_and_quan)
# 	print(reduce(lambda acc, pair: acc+(int(pair[0])*int(pair[1])), filtred, 0))


# with open('TEST_DATA.txt', encoding='utf-8') as file:
#     print('Repeat after me:', file.readline().strip())
#     for line in file:
#         print(line.strip() + '!')

# with open("TEST_DATA.txt", encoding="utf-8") as torrent:
#     print(*reversed(list(map(str.strip, torrent.readlines()))), sep="\n")


# with open("TEST_DATA.txt", encoding="utf-8") as torrent:
# 	strings = tuple(map(str.strip, list(torrent)))
# 	max_string = max(strings, key=len)
# 	result = list(filter(lambda string: True if len(string) >= len(max_string) else False, strings))
# 	print(*result, sep="\n")

# with open("TEST_DATA.txt", encoding="utf-8") as torrent:
# 	group_nums = [item.strip().split() for item in torrent.read().split('\n')]
# 	# group_nums = [item.strip().split() for item in torrent.readlines()]
# 	# print(group_nums)
# 	print(*list(map(lambda item: sum(list(map(int, item))), group_nums)), sep="\n")
# 	# print(list(map(lambda item: sum(list(map(int, item))), group_nums)))
	
# 	# map(int, torrent.read().split())


import string

sum_, asci = 0, string.ascii_letters
with open("TEST_DATA.txt", encoding="utf-8") as torrent:
	nums = [item.strip().split() for item in torrent]	
	clear = [[int(num) for num in item if num.isdigit()] for item in nums]
	mixed = [[num for num in item if num.isdigit() is False] for item in nums]

result = list()
for pair in enumerate(mixed):
	if len(pair[1]) > 0:
		before_char = pair[1][0]
	result.append([])
	for item in pair[1]:
		result[pair[0]].append("-")
		for char in item:
			# print(char, end="|")
			if char.isdigit():
				result[pair[0]].append(char)
			else:
				result[pair[0]].append("-")

result = map(lambda item: "".join(item).split("-"), result)
result = list(map(lambda pack: list(filter(lambda item: any(item), pack)), result))
post_result = list()

for item in result:
	if len(item) > 1:
		print(item)
		for elem in item:
			post_result.append(int(elem))

clear = [num for pack in clear for num in pack]

print(sum(post_result) + sum(clear))


# print(nums)
# print(clear)
# print(mixed)
# print(result)