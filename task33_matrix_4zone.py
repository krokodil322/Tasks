size = int(input())
matrix = [[int(row) for row in input().split()] for _ in range(size)]

zone = [[], [], [], []]
for i in range(size):
	for j in range(size):
		if i = n - j - 1
		if i < j and size > i + j + 1:
			zone[0].append(matrix[i][j])
		if i < j and size < i + j + 1:
			zone[1].append(matrix[i][j])
		if i > j and size < i + j + 1:
			zone[2].append(matrix[i][j])
		if i > j and size > i + j + 1:
			zone[3].append(matrix[i][j])

print(f"Верхняя четверть: {zone[0]}")
print(f"Правая четверть: {zone[1]}")
print(f"Нижняя четверть: {zone[2]}")
print(f"Левая четверть: {zone[3]}")

# print(f"Верхняя четверть: {sum(zone[0])}")
# print(f"Правая четверть: {sum(zone[1])}")
# print(f"Нижняя четверть: {sum(zone[2])}")
# print(f"Левая четверть: {sum(zone[3])}")
