


# size = len(list(input()))
# if size != 1:
# 	print( f"{int(size * 0.6)} р. " + f"{int( round((size * 0.6) % ((size * 0.6) // 1) * 100 ))} коп." )
# else:
# 	print("0 р. " + "60 коп.")

size = len(list("Привет, как дела?!")) * 60
print( f"{int(size // 100)} р. " + f"{int(size % 100)} коп." )

# print((10.8 % 10) * 10)

input()