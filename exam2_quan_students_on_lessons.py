
student_all_time = [set(["".join(input()) for _ in range(int(input()))]) for _ in range(int(input()))]


result = student_all_time[0]
for index in range(1, len(student_all_time)):
	result.intersection_update(student_all_time[index])
print(*sorted(result), sep="\n")
