
fridges = [input() for index in range(0, int(input()))]
for index in range(0, len(fridges)):
	code = ['a', 'n', 't', 'o', 'n']
	for char in fridges[index]:
		if char == code[0]:
			code.remove(char)
			# print(code)
		if len(code) == 0:
			print(index + 1, end=" ")
			break

		
