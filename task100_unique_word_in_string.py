
result = dict()
for word in "".join([char.lower() for char in input() if char not in ['.', ',', '!', '?']]).split():
	if result.get(word, None) is None:
		result[word] = 1
	else:
		result[word] += 1
min_elem = min(result.values())
print(sorted([word for word in result if result[word] == min_elem])[0])