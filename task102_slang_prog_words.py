

slang_words = dict()
for quan_termin in range(int(input())):
	input_data = [word for word in input().split(": ")]
	slang_words.setdefault(input_data[0].lower(), input_data[1])
input_data = list()
for quan_termin in range(int(input())):
	input_data.append(input().lower())
for response in input_data:
	if slang_words.get(response, None) is not None:
		print(slang_words[response])
	else:
		print("Не найдено")
