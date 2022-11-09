import random

table = set()
while len(table) != 25:
	table.add(random.randint(1, 75))

table = list(table)
table[12] = 0

for index in range(1, len(table) + 1):
	# print("\t\t\t" + str(index))
	print(str(table[index - 1]).ljust(3), end=" ")
	if index % 5 == 0:
		print()
		
	




