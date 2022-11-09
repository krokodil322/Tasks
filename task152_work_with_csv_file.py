
with open("data.txt", encoding="utf-8") as torrent:
	keys = [item.strip() for item in torrent.readline().split(",")]
	values = [item.strip().split(',') for item in torrent.readlines()]

# def read_csv() -> list:
# 	data = list()
# 	for pack in enumerate(values):
# 		data.append({})
# 		for key, value in zip(keys, pack[1]):
# 			data[pack[0]].setdefault(key, value)
# 	return data



def read_csv() -> list:
	with open("data.csv", encoding="utf-8") as torrent:
		keys = [item.strip() for item in torrent.readline().split(",")]
		values = [item.strip().split(',') for item in torrent.readlines()]
	data = list()
	for pack in enumerate(values):
		data.append({})
		for key, value in zip(keys, pack[1]):
			data[pack[0]].setdefault(key, value)
	return data

print(read_csv())