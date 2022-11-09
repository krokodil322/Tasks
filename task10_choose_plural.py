

def choose_plural(number, list_of_forms):
	if number%100 == 1 and number != 11:
		return str(number) + ' ' + list_of_forms[0]
	elif number%100 > 4:
		return str(number) + ' ' + list_of_forms[2]
	elif 2<=number%100<=4 and not (number in [12, 13, 14]):
		return str(number) + ' ' + list_of_forms[1]
	return str(number) + ' ' + list_of_forms[2]

print(choose_plural(21, ('пример', 'примера', 'примеров')))
print(choose_plural(8, ('яблоко', 'яблока', 'яблок')))
print(choose_plural(512312, ('цент', 'цента', 'центов')))
print(choose_plural(92, ('гвоздь', 'гвоздя', 'гвоздей')))
print(choose_plural(59, ('помидор', 'помидора', 'помидоров')))