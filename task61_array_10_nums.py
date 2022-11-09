
string = input().split()

resting_elem, status = set(string[0]), True
for item in string:
	if resting_elem != set(item):
		status = False
		break


if status:
	print("YES")
else:
	print("NO")