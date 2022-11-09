import string

# def filter_for_string(num) -> bool:
# 	asci_data, status = string.ascii_letters + '-', True
# 	for char in num:
# 		if char in asci_data:
# 			status = False
# 			break
# 	if status:
# 		if len(num.split(".")) < 3:
# 			return True
# 		else:
# 			return False

# is_non_negative_num = lambda num: True if filter_for_string(num) else False

# is_non_negative_num = lambda num: True if (num.replace(".", "", 1)).isdigit() else False

# print(is_non_negative_num('10.34ab'))
# print(is_non_negative_num('10.45'))
# print(is_non_negative_num('-18'))
# print(is_non_negative_num('-34.67'))
# print(is_non_negative_num('987'))
# print(is_non_negative_num('abcd'))
# print(is_non_negative_num('123.122.12'))
# print(is_non_negative_num('123.122'))


is_num = lambda num: True if (num.replace(".", "", 1).replace('-', "", 1)).isdigit() else False
print(is_num('a.6'))
print(is_num('1-1'))
print(is_num('10.34ab'))
print(is_num('10.45'))
print(is_num('-18'))
print(is_num('-34.67'))
print(is_num('987'))
print(is_num('abcd'))
print(is_num('123.122.12'))
print(is_num('-123.122'))
print(is_num('--13.2'))