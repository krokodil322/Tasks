
with open("class_scores.txt", encoding="utf-8") as take, open("new_scores.txt", 'w', encoding="utf-8") as put:
	data, check_points = dict(), lambda val: 100 if val + 5 > 100 else val + 5
	for item in take.readlines():
		key, value = item.split()
		data.setdefault(key, check_points(int(value)))

	put.writelines([f"{key} {value}\n" for key, value in data.items()])
