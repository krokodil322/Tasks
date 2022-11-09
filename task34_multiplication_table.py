
row = int(input())
column = int(input())
multiplication_table = [[0 for c in range(column)] for r in range(row)]
for r in range(row):
	for c in range(column):
		multiplication_table[r][c] = r * c
for r in range(row):
	for c in range(column):
		print(str(multiplication_table[r][c]).ljust(3), end="")
	print()

