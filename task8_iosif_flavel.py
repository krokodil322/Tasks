
# data_input = [10, 5]

# circle = [number for number in range(1, data_input[0] + 1)]
# circle_buffer = circle.copy()
# elimination_order_list = []

# while len(circle) > 1:
# 	print(f"Первоначальный список: {circle}")
# 	counter = 1
# 	if len(circle) < data_input[1]:
# 		circle.insert(0, data_input[1] + 1)
# 	for element in circle:
# 		# print(f"Номер итерации: {counter} " + f"Отношение counter '%' data_input[1]: {counter % data_input[1]}", end="")
# 		# print(" Элемент: " + str(element))
# 		if counter < len(circle) and data_input[1] > len(circle):
# 			counter = data_input[1]
# 		if counter % data_input[1] == 0 and len(circle_buffer) > 1:
# 			elimination_order_list.append(element)
# 			circle_buffer.remove(element)
# 		counter += 1
# 	circle = circle_buffer.copy()
# 	print(f"Удалёны по порядку: {elimination_order_list}")
# 	print(f"Осталось: {circle_buffer}")
# 	elimination_order_list = []



n=int(input())
k=int(input())
res=0
for i in range(1, n+1):
    res = (res + k) % i 
print(res + 1)

