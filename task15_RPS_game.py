options = ["камень", "ножницы", "бумага"]
# timur, ruslan = input(), input()
# if ruslan == timur:
# 	print("ничья")
# elif ruslan == "камень" and timur == "ножницы":
# 	print("Руслан")
# elif ruslan == "ножницы" and timur == "бумага":
# 	print("Руслан")
# elif ruslan == "бумага" and timur == "камень":
# 	print("Руслан")
# elif timur == "камень" and ruslan == "ножницы":
# 	print("Тимур")
# elif timur == "ножницы" and ruslan == "бумага":
# 	print("Тимур")
# elif timur == "бумага" and ruslan == "камень":
# 	print("Тимур")

# for cycle in range(0, len(options)):
# 	if ruslan == options[0] and timur == options[1]

from itertools import product
combo_list = list(product(["камень", "ножницы", "бумага"], repeat=2))
gamers = (input(), input())
if gamers == combo_list[1] or gamers == combo_list[5] or gamers == combo_list[6]:
	print("Тимур")
elif gamers == combo_list[2] or gamers == combo_list[3] or gamers == combo_list[7]:
	print("Руслан")
elif gamers == combo_list[0] or gamers == combo_list[4] or gamers == combo_list[8]:
	print("ничья")