buttons = {
	'0': [" "],
    '1': [".", ",", "?", "!", ":"],
    '2': ["A", "B", "C"],
    '3': ["D", "E", "F"],
    '4': ["G", "H", "I"],
    '5': ["J", "K", "L"],
    '6': ["M", "N", "O"],
    '7': ["P", "Q", "R", "S"],
    '8': ["T", "U", "V"],
    '9': ["W", "X", "Y", "Z"]
}

buttons_press = str()
#записываем все символы с верхнем регистре
#и перебираем их
for char in [char.upper() for char in input()]:
	#перебираем пару ключ\значение словаря
	for key, value in buttons.items():
		#если символ в списке значения словаря
		if char in value:
			#печатаем ключ столько раз сколько
			#значений было до символа в списке словаря
			for _ in value[0:value.index(char) + 1]:
				buttons_press += key
print(buttons_press)

