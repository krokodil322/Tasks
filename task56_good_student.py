

students = []
for item in [[item for item in input().split()] for _ in range(int(input()))] :
	item[1] = int(item[1])
	students.append(tuple(item))
for item in students:
	print(item[0], item[1], sep=" ")
input()
for item in students:
	if item[1] == 4 or item[1] == 5:
		print(item[0], item[1], sep=" ")

