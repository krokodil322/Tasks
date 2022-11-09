
diapason, statuses = map(lambda num: list(str(num)), range(int(input()), int(input()))), list()


for index, item in list(enumerate(diapason)):
	num = int("".join(item))
	statuses.append([])
	for digit in item:
		if int(digit) != 0 and num % int(digit) == 0:
			statuses[index].append(True)
		else:
			statuses[index].append(False)
	if all(statuses[index]):
		print(num, end=" ")

