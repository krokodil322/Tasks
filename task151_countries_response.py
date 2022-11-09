
with open("population.txt", encoding="utf-8") as torrent:
	result = [item.strip() for item in torrent.readlines()]

result = filter(lambda pack: True if (pack[0] == 'G') and (int(pack.split('\t')[1])) > 5*10**5 else False, result)

for item in result:
	print(item.split('\t')[0])