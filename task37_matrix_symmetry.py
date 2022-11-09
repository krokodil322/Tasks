НИХУЯ НЕ РАБОТАЕТ ГОВНО
# from math import floor

# size = int(input())
# matrix = [[int(item) for item in input().split()] for _ in range(size)]


# zone = [[], [], [], [], []]
# #Заполняем срезы зон матрицы
# for i in range(size):
# 	for j in range(size):
# 		if i < j and size > i + j + 1:
# 			zone[0].append(matrix[i][j])
# 		if i < j and size < i + j + 1:
# 			zone[4].append(matrix[i][j])
# 		if i > j and size < i + j + 1:
# 			zone[3].append(matrix[i][j])
# 		if i > j and size > i + j + 1:
# 			zone[1].append(matrix[i][j])
# 		if j == size - i - 1:
# 			zone[2].append(matrix[i][size - i - 1])
# #Сравниваем поэлементно
# # #ДЛЯ ПОБ. ДИАГОНАЛИ
# # if len(zone[2]) % 2 != 0:
# # 	#удаляем срединый элемент(т.к он может быть любым)
# # 	zone[2].pop(floor(size / 2))
# # sample = zone[2][0]
# # for item in zone[2]:
# # 	if sample != item:
# # 		print("NO")
# # 		status = False
# # 		break
# zone.pop(2)
# print(zone)
# if size > 3:
# 	if zone[0][0:round(len(zone[0])/2):1] != zone[1][0:round(len(zone[1])/2):1]:
# 		print("NO")
# 	else:
# 		if zone[0][round(len(zone[0])/2)::1] != zone[1][-1:-round(len(zone[1])/2)-1:-1]:
# 			print("NO")
# 		else:
# 			if zone[2][0:round(len(zone[2])/2):1] != list(reversed(zone[3][0:round(len(zone[2])/2):1])):
# 				print("NO")
# 			else:
# 				print("YES")
# else:
# 	if zone[0] != zone[2]:
# 		print("NO")
# 	else:
# 		if zone[1] != zone[-1]:
# 			print("NO")
# 		else:
# 			print("YES")




# # print(zone)