def merge(response: list) -> dict:
	result = dict()
	for item in response:
		for key, value in item.items():
			result.setdefault(key, set()).add(value)

	return result

print(merge([{'a': 1, 'b': 2}, {'b': 10, 'c': 100}, {'a': 1, 'b': 17, 'c': 50}, {'a': 5, 'd': 777}]))


