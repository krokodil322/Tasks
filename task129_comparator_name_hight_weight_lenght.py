athletes = [('Дима', 10, 130, 35), ('Тимур', 11, 135, 39), ('Руслан', 9, 140, 33), 
			('Рустам', 10, 128, 30), ('Амир', 16, 170, 70), ('Рома', 16, 188, 100), 
			('Матвей', 17, 168, 68), ('Петя', 15, 190, 90)]

def name(athlet: list) -> list:
	return athlet[0]

def age(athlet: list) -> list:
	return athlet[1]

def lenght(athlet: list) -> list:
	return athlet[2]

def weight(athlet: list) -> list:
	return athlet[3]

def show_data(athletes: list) -> list:
	for item in athletes:
		print(*item)
		
functions = {'1': name, '2': age, '3': lenght, '4': weight}


show_data(sorted(athletes, key=functions[input()]))