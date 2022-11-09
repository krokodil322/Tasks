str1 = "Hellowqwer"
str2 = "llow"

# print(str1.find(str2))

# print(str1[1:])

# print(list("".join(str1[1:])))

slice_str1 = str1[2:]
index_begin = str1.find(str2)

str1 = str1.replace(str2, '*'*len(str2))

print(str1)
print()
print( f"{ '*'*len(str2) }" )
print(str1)
# print(index_begin, index_end, slice_str1, sep="\n")