
# phone_book = dict()
# for item in [[str(value).lower() for value in input().split()] for _ in range(int(input()))]:
# 	if phone_book.get(item[1], None) is None:
# 		phone_book[item[1]] = [item[0]]
# 	else:
# 		phone_book[item[1]].append(item[0])
# for name in [name.lower() for _ in range(int(input())) for name in input().split()]:
# 	if phone_book.get(name, None) is not None:
# 		print(*phone_book[name])
# 	else:
# 		print("абонент не найден")

phone_book = dict()
for item in [[str(value).lower() for value in input().split()] for _ in range(int(input()))]:
	phone_book.setdefault(item[1], []).append(item[0])
	print(phone_book)

# for name in [name.lower() for _ in range(int(input())) for name in input().split()]:
# 	if phone_book.get(name, None) is not None:
# 		print(*phone_book[name])
# 	else:
# 		print("абонент не найден")
