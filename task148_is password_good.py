import string

HIGH, LOW, NUM, password = string.ascii_uppercase, string.ascii_lowercase, string.digits, list(input())

status = list()
if len(password) >= 7:
	status.append(any(map(lambda char: True if char in HIGH else False, password)))
	status.append(any(map(lambda char: True if char in LOW else False, password)))
	status.append(any(map(lambda char: True if char in NUM else False, password)))
	print("YES" if all(status) else "NO")
else:
	print("NO")