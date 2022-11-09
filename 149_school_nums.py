


students = list()
for index in range(int(input())):
	students.append(dict())
	for _ in range(int(input())):
		name, grade = input().split()
		students[index].setdefault(name, int(grade))

result = list()
for class_ in students:
	result.append(any(map(lambda grade: True if grade == 5 else False, class_.values())))

print("YES" if all(result) else "NO")