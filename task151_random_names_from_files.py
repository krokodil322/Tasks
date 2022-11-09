from random import shuffle


# with open("file.txt", encoding="utf-8") as torrent1, open("file2.txt", encoding="utf-8") as torrent2:
# 	first_names, last_names = [item.strip() for item in torrent1], [item.strip() for item in torrent2]
# 	shuffle(first_names), shuffle(last_names)

# result = dict(zip(first_names, last_names))
# for key, value in result.items():
# 	print(key, value, sep=" ")

with open("file.txt", encoding="utf-8") as torrent1, open("file2.txt", encoding="utf-8") as torrent2:
	first_names, last_names = [item.strip() for item in torrent1], [item.strip() for item in torrent2]
	shuffle(first_names), shuffle(last_names)

result, counter = dict(zip(first_names, last_names)), 0
for key, value in result.items():
	if counter == 3:
		break
	print(key, value, sep=" ")
	counter += 1