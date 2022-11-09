import random

quan, lenght = int(input()), int(input())
for _ in range(quan):
	password = list()
	while len(password) != lenght:
		status = random.randint(0, 2)
		if status == 0:
			char = chr(random.randint(65, 90))
			if (char not in password) and (char not in ['O', 'I']):
				password.append(char)
		elif status == 1:
			char = chr(random.randint(97, 122))
			if (char not in password) and (char not in ['o', 'l']):
				password.append(char)
		else:
			char = chr(random.randint(48, 57))
			if (char not in ['1', '0']):
				password.append(char)
	print("".join(password))
