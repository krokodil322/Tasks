list_nums = [5, -8, 3, 7, -10, 1]
list_nums = list(map(abs, list_nums)) 
print(list_nums)

def num_plus_one(num: int) -> int:
	"""ФУНКЦИЯ УВЕЛИЧИВАЕТ ЧИСЛО НА 1"""
	"""И ВОЗВРАЩАЕТ УВЕЛИЧЕННОЕ ЧИСЛО"""
	return num + 1

list_nums = [1, 2, 3, 4, 5]
list_nums = list(map(num_plus_one, list_nums))
print(list_nums)

def test_map(num: int) -> int:
	if num > 10:
		return num

list_nums = [14, 0, 10, 24, 75, -20]
list_nums = list(map(test_map, list_nums))
print(list_nums)

def test_filter(num: int) -> bool:
	return num > 10

list_nums = [14, 0, 10, 24, 75, -20]
list_nums = list(filter(test_filter, list_nums))
print(list_nums)

print(list)

