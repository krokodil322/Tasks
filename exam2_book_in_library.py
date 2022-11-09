size_lib = int(input())
size_list = int(input())
# book_in_lib = ["".join(input()) for _ in range(size_lib)]
# book_in_list = ["".join(input()) for _ in range(size_list)]

# for book_list in book_in_list:
# 	if book_list in book_in_lib:
# 		print("YES")
# 	else:
# 		print("NO")

book_in_lib = {"".join(input()) for _ in range(size_lib)}
book_in_list = ["".join(input()) for _ in range(size_list)]
book_in_lib.intersection_update(book_in_list)

for book_list in book_in_list:
	if book_list in book_in_lib:
		print("YES")
	else:
		print("NO")

print()
