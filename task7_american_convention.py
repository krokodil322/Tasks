

user_num_list, factor = list(input("Введи число для разделения: "))[-1::-1], 0
for cycle in range(1, len(user_num_list) + 1):
	if cycle % 3 == 0:
		user_num_list.insert(cycle + factor, ",")
		if user_num_list[-1] == ",":
			user_num_list.pop(-1)
		factor += 1
print("".join(user_num_list[-1::-1]))





