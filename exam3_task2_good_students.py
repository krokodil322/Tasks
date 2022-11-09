
with open("grades.txt", encoding="utf-8") as torrent:
	students = list()
	for pack in enumerate(torrent.readlines()):
		students.append({})
		elem = pack[1].split()
		students[pack[0]].setdefault(elem[0], elem[1:])

statuses = list()
for student in enumerate(students):
	values = student[1].values()
	statuses.append([])
	for points in values:
		for point in points:
			if int(point) >= 65:
				statuses[student[0]].append(True)
			else:
				statuses[student[0]].append(False)

print(sum([1 for status in statuses if all(status)]))
