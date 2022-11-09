import random


password = str()
for _ in range(int(input())):
	status = random.randint(0, 1)
	if status == 1:
		password += chr(random.randint(65, 90))
	else:
		password += chr(random.randint(97, 122))
print(password)


