from itertools import product
combo_list = list(product(["камень", "ножницы", "бумага", "ящерица", "Спок"], repeat=2))
gamers = (input(), input())
if gamers in [combo_list[index] for index in [1, 3, 7, 8, 10, 14, 17, 19, 20, 21]]:
	print("Тимур")
elif gamers in [combo_list[index] for index in [2, 4, 5, 9, 11, 13, 15, 16, 22, 23]]:
	print("Руслан")
elif gamers in [combo_list[index] for index in [0, 6, 12, 18, 24]]:
	print("ничья")