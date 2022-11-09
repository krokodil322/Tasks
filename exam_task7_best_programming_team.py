
with open("programm.txt", encoding="utf-8") as torrent:
	data = torrent.readlines()

before_lines, result = data[0], list()
for row in data:
	if row.find("def") != -1 and before_lines.find('#') == -1:
		result.append(row)
	if before_lines != row:
		before_lines = row

for item in result:
	item = item.split()
	print(item[1].split('(')[0])