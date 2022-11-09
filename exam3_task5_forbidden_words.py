
with open("forbidden_words.txt", encoding="utf-8") as torrent:
	forbidden = "".join(torrent.readlines()).split()

with open(input(), encoding="utf-8") as torrent:
	words = "".join(torrent.readlines())

original = words
for word_f in forbidden:
	words = words.lower().replace(word_f, '*'*len(word_f))

result = str()
for orig, diff in zip(original, words):
	if orig.isupper() and diff.islower():
		result += orig
	else:
		result += diff
		
print(result)