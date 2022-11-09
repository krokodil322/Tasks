
checks, result = dict(), dict()
for _ in range(int(input())):
	input_data = input().split()
	if checks.get(input_data[0]) is None or checks.get(input_data[0]).get(input_data[1]) is None:
		checks.setdefault(input_data[0], dict()).setdefault(input_data[1], input_data[2])
	else:
		checks[input_data[0]][input_data[1]] = str(int(checks.get(input_data[0]).get(input_data[1])) + int(input_data[2]))
	
for key1, value1 in sorted(checks.items()):
	print(key1 + ':')
	for key2, value2 in sorted(value1.items()):
		print(key2, value2, sep=" ")