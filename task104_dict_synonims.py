dict_synonyms = dict()
for _ in range(int(input())):
	words = [word for word in input().split()]
	dict_synonyms[words[0]] = words[1]

word_input = input()
for key, value in dict_synonyms.items():
	if word_input == value:
		print(key)
	elif word_input == key:
		print(value)