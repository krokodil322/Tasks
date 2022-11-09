func = lambda string: True if (list(string.lower())[0] == 'a') and (list(string.lower())[-1] == 'a') else False

# print(func('abcd'))
# print(func('bcda'))
# print(func('abcda'))
# print(func('Abcd'))
# print(func('bcdA'))
# print(func('abcdA'))

S = ' 123'
# S = S.replace(".", "", 1)
# print(S)
print(S.isdigit())

