# info_list = [('name', 'Timur'), ('age', 28), ('job', 'Teacher')]  # список кортежей
# info_dict = dict(info_list)  # создаем словарь на основе списка кортежей
# print(info_dict)


# mydict = dict.fromkeys(['A', 'B', 'C', 'D', 'E'], 'NULL')
# print(mydict)

# keys = ["first_name", "last_name", "date_of_birth"]
# values = ["Vasily", "Petrov", "15-09-1987"]
# data_person = dict(zip(keys, values))
# print(data_person)

# capitals = {'Россия': 'Москва', 'Франция': 'Париж', 'Чехия': 'Прага'}

# for element in capitals:
#     print(element)

# users = [{'name': 'Todd', 'phone': '551-1414', 'email': 'todd@gmail.com'},
#          {'name': 'Helga', 'phone': '555-1618', 'email': 'helga@mail.net'},
#          {'name': 'Olivia', 'phone': '449-3141', 'email': ''},
#          {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@gmail.net'},
#          {'name': 'Ruslan', 'phone': '422-145-9098', 'email': 'rus-lan.cha@yandex.ru'},
#          {'name': 'John', 'phone': '233-421-32', 'email': ''},
#          {'name': 'Lara', 'phone': '+7998-676-2532', 'email': 'g.lara89@gmail.com'},
#          {'name': 'Alina', 'phone': '+7948-799-2434', 'email': 'ali.ch.b@gmail.com'},
#          {'name': 'Robert', 'phone': '420-2011', 'email': ''},
#          {'name': 'Riyad', 'phone': '128-8890-128', 'email': 'r.mahrez@mail.net'},
#          {'name': 'Khabib', 'phone': '+7995-600-9080', 'email': 'kh.nurmag@gmail.com'},
#          {'name': 'Olga', 'phone': '6449-314-1213', 'email': ''},
#          {'name': 'Roman', 'phone': '+7459-145-8059', 'email': 'roma988@mail.ru'},
#          {'name': 'Maria', 'phone': '12-129-3148', 'email': 'm.sharapova@gmail.com'},
#          {'name': 'Fedor', 'phone': '+7445-341-0545', 'email': ''},
#          {'name': 'Tim', 'phone': '242-449-3141', 'email': 'timm.ggg@yandex.ru'}]
# names = list()
# for user in users:
#     if list(user['phone'])[-1] == '8':
#         names.append(user['name'])
# print(*sorted(names))


# users = [{'name': 'Todd', 'phone': '551-1414', 'email': 'todd@gmail.com'},
#          {'name': 'Helga', 'phone': '555-1618'},
#          {'name': 'Olivia', 'phone': '449-3141', 'email': ''},
#          {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@gmail.net'},
#          {'name': 'Ruslan', 'phone': '422-145-9098', 'email': 'rus-lan.cha@yandex.ru'},
#          {'name': 'John', 'phone': '233-421-32', 'email': ''},
#          {'name': 'Lara', 'phone': '+7998-676-2532', 'email': 'g.lara89@gmail.com'},
#          {'name': 'Alina', 'phone': '+7948-799-2434'},
#          {'name': 'Robert', 'phone': '420-2011', 'email': ''},
#          {'name': 'Riyad', 'phone': '128-8890-128', 'email': 'r.mahrez@mail.net'},
#          {'name': 'Khabib', 'phone': '+7995-600-9080', 'email': 'kh.nurmag@gmail.com'},
#          {'name': 'Olga', 'phone': '6449-314-1213', 'email': ''},
#          {'name': 'Roman', 'phone': '+7459-145-8059'},
#          {'name': 'Maria', 'phone': '12-129-3148', 'email': 'm.sharapova@gmail.com'},
#          {'name': 'Fedor', 'phone': '+7445-341-0545', 'email': ''},
#          {'name': 'Tim', 'phone': '242-449-3141', 'email': 'timm.ggg@yandex.ru'}]
# # result = list()
# # for user in users:
# # 	if "email" in user.keys():
# # 		if user["email"] == "":
# # 			result.append(user["name"])
# # 	else:
# # 		result.append(user["name"])
# # print(*sorted(result))


# # info = {'name': 'Bob',
# #         'age': 25,
# #         'job': 'Dev'}
# # print(info.get("age", None))
# # print(info.get("last_name", None))


# buffer_users = users.copy()
# users = list()
# for user in buffer_users:
#     if user.get("email", None) != None and user.get("email", None) != "":
#         print(user)


# numbers = [9, 8, 32, 1, 10, 1, 10, 23, 1, 4, 10, 4, 2, 2, 2, 2, 1, 10, 1, 2, 2, 32, 23, 23]
# #Создаём словарь для записи результата
# result = dict()
# for num in numbers:
#     #В левой части создаём новый ключ под именем уникального числа:
#     #В правой части мы достаём из словаря result значение которое повторилось
#     #И складываем в под этим ключом
#     result[num] = result.get(num, 0) + 1

# print(result)

names_worker = {"id3": "Bob", "id4": "Vasily"}
names_buyer = {"id1": "Petor", "id2": "Alexsandr"}
names_worker.update(names_buyer)

print(names_worker)