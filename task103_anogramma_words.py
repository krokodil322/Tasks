	
word_chars1, word_chars2 = dict(), dict()

for char in [char.lower() for word in input().split() for char in word if char not in ['!', '?', ',', ':']]:
	if word_chars1.get(char, None) is None:
		word_chars1[char] = 1
	else:
		word_chars1[char] += 1
for char in [char.lower() for word in input().split() for char in word if char not in ['!', '?', ',', ':']]:
	if word_chars2.get(char, None) is None:
		word_chars2[char] = 1
	else:
		word_chars2[char] += 1
status = True
for key1, key2 in zip(sorted(word_chars1.keys()), sorted(word_chars2.keys())):
	#1-ОЕ: ПРОВЕРКА НА КОЛ-ВО СИМОЛОВ, ЕСЛИ КОЛ-ВО НЕ РАВНО, ТО СЛОВА УЖЕ НЕ АНОГРАММЫ
	#2-ОЕ: ПРОВЕРКА НА НАЛИЧИЕ КЛЮЧА, ЕСЛИ КЛЮЧА ВО ВТОРОМ НЕТУ, ТО СЛОВА НЕ АНОГРАММЫ
	if (word_chars1.get(key1) != word_chars2.get(key2)) or (word_chars2.get(key1) is None):
		status = False
print("YES" if status else "NO")


# word_chars2 = [char for char in input()]

# print(word1, word2, sep="\n")

