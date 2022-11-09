numbers = [34, 10, -4, 6, 10, 23, -90, 100, 21, -35, -95, 1, 36, -38, -19, 1, 6, 87]
result = {index: num**2 for num, index in zip(numbers, range(len(numbers)))}
print(result)

# colors = {
# 			'c1': 'Red', 'c2': 'Grey', 'c3': None, 'c4': 'Green', 'c5': 'Yellow', 
# 			'c6': 'Pink', 'c7': 'Orange', 'c8': None, 'c9': 'White', 'c10': 'Black', 
# 			'c11': 'Violet', 'c12': 'Gold', 'c13': None, 'c14': 'Amber', 'c15': 'Azure', 
# 			'c16': 'Beige', 'c17': 'Bronze', 'c18': None, 'c19': 'Lilac', 'c20': 'Pearl', 
# 			'c21': None, 'c22': 'Sand', 'c23': None
# 		 }
# result = {key: value for key, value in colors.items() if value is not None}
# print(result)

favorite_numbers = {
						'timur': 17, 'ruslan': 7, 'larisa': 19, 'roman': 123, 
						'rebecca': 293, 'ronald': 76, 'dorothy': 62, 'harold': 36, 
						'matt': 314, 'kim': 451, 'rosaly': 18, 'rustam': 89, 
						'soltan': 111, 'amir': 654, 'dima': 390, 'amiran': 777, 
						'geor': 999, 'sveta': 75, 'rita': 909, 'kirill': 404, 
						'olga': 271, 'anna': 55, 'madlen': 876

					}

result = {key: value for key, value in favorite_numbers.items() if len(list(str(value))) == 2}
print(result)
print(len(result))

# result = {key: value for key, value in favorite_numbers.items() if value / 10 < 10 and value / 10 > 1}
# print(result)
# print(len(result))

s = '1:men 2:kind 90:number 0:sun 34:book 56:mountain 87:wood 54:car 3:island 88:power 7:box 17:star 101:ice'

result = {item.split(':')[0]: item.split(':')[1] for item in s.split()}
print(result)