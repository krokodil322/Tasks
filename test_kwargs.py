

# def division_and_sum(**kwargs):
# 	print(kwargs)
# 	return sum(kwargs.values())


# print(division_and_sum(a=2, b=4, c=8, d=23, e=-5))
# print(division_and_sum(**{'a': 3, 'b': 8, 'c': 15}))


# def mean(*args) -> float:
# 	if len(args) == 0:
# 		return 0.0

# 	result = list()
# 	for item in args:
# 		if (isinstance(item, (int, float)) is True and (isinstance(item, bool)) is False):
# 			result.append(item)

# 	if len(result) != 0:
# 		return sum(result) / len(result)
# 	else:
# 		return 0.0

# print(mean(0))
# print(mean())
# print(mean(7))
# print(mean(1.5, True, ['stepik'], 'beegeek', 2.5, (1, 2)))
# print(mean(True, ['stepik'], 'beegeek', (1, 2)))
# print(mean(-1, 2, 3, 10, ('5')))
# print(mean(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
# # status = 4

# # print(isinstance(status, bool))

# def greet(name_person: str, *args) -> str:
# 	result = "Hello," + " " + name_person
# 	for name, index in zip(args, range(len(args))):
# 		if len(args) - 1 >= index:
# 			result += " " + "and"
# 		result += " " + name
# 	return result + '!'

# print(greet('Timur'))
# print(greet('Timur', 'Roman'))
# print(greet('Timur', 'Roman', 'Ruslan'))
points = [(1, -1), (2, 3), (-10, 15), (10, 9), (7, 18), (1, 5), (2, -4)]
print(points)

def sum_element(pair: tuple) -> int:
	return pair[0] + pair[1]

points = sorted(points, key=sum_element)
print(points)

def print_data():
	def print_head_data():
		print("Head data")
	return print_head_data

phd = print_data()

phd()