# file1.txt
# file2.txt
# file3.txt



data = list()
for file in [name for _ in range(int(input())) for name in input().split()]:
	with open(file, encoding="utf-8") as torrent:
		data.append([file + '\n'])
		data.append(torrent.readlines())
print(data)
data = [[item.strip() + '\n' for item in pack] for pack in data]
data[-1][-1] = data[-1][-1].strip()

with open("output.txt", 'w', encoding="utf-8") as torrent:
	for pack in data:
		torrent.writelines(pack)