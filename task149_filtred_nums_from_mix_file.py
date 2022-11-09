

with open("TEST_DATA.txt", encoding="utf-8") as torrent:
	result = [[item.strip()] for item in torrent.readlines()]

filtred = list()
for item in result:
	pre_res = str()
	for elem in item:
		if elem.isdigit():
			filtred.append(elem)
		else:
			for char in elem:
				if char.isdigit():
					pre_res += char
				else:
					pre_res += "-"
			filtred.append(pre_res)
result = ["".join(item).split("-") for item in filtred]
result = [int(elem) for item in result for elem in item if elem.isdigit() ]
print(sum(result))



