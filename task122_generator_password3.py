import random
import string

CHAR_UP = list(string.ascii_uppercase)
CHAR_DOWN = list(string.ascii_lowercase)
NUMS = list(string.digits)

def check_chars(password: list) -> bool:
	"""ВОЗВРАЩАЕТ TRUE, ЕСЛИ В ВХОДЯЩЕМ СПИСКЕ
	   ЕСТЬ ХОТЯ БЫ ОДИН СИМОЛ ВЕРХНЕГО, 
	   НИЖНЕГО РЕГИСТРА И ЧИСЛО, ЕСЛИ НЕТ, ТО FALSE"""
	status_chars = {"up": False, "down": False, "num": False}
	for char in password:
		if char in CHAR_UP:
			status_chars["up"] = True
		if char in CHAR_DOWN:
			status_chars["down"] = True
		if char in NUMS:
			status_chars["num"] = True
		
	for value in status_chars.values():
		if value is False:
			return False

	return True


def generator_passwords(lenght: int) -> str:
	password= list()
	while True:
		while (len(password) != lenght):
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
		if check_chars(password) is True:
			return "".join(password)
		else:
			password = list()


def dispathcer(quan: int, lenght: int) -> None:
	for _ in range(quan):
		print(generator_passwords(lenght))
	return None

dispathcer(int(input()), int(input()))