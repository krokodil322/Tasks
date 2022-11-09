
with open("words.txt", encoding="utf-8") as torrent:
	data = "".join(torrent.readlines()).split()

max_lenght, result = max(list(map( lambda word: len(list(word)), data))), list()
for word in data:
	if len(word) >= max_lenght:
		result.append(word)
print(*result, sep="\n")