import string

asci, counter = string.ascii_letters, list()
with open("file.txt", encoding="utf-8") as torrent:
	data = [item.strip() for item in torrent.readlines()]

counter.append(sum([1 for item in data for char in item if char in asci]))
counter.append(sum([len(item.split()) for item in data]))
counter.append(len(data))

print(f"Input file contains:\n{counter[0]} letters\n{counter[1]} words\n{counter[2]} lines")