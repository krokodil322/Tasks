encrypt_word_chars = dict()
encrypt_word = list(input())
for char in encrypt_word:
	if encrypt_word_chars.get(char, None) is None:
		encrypt_word_chars[char] = 1
	else:
		encrypt_word_chars[char] += 1
chars_dict_for_word = dict()
for _ in range(int(input())):
	item = input().split(': ')
	chars_dict_for_word[item[0]] = int(item[1])

test_list = list()
for _ in range(sum(list(chars_dict_for_word.values()))):
	for chars1, chars2 in zip(chars_dict_for_word.items(), encrypt_word_chars.items()):
		if chars2[0] in encrypt_word:
			encrypt_word[encrypt_word.index(chars2[0])] = chars1[0]
			test_list.append(chars1[0])
			

print("".join(encrypt_word))
print(test_list)
