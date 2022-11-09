
sum_ = lambda a, b: a + b
print(sum_(3, 5))
print()

points = [(1, -1), (2, 3), (-10, 15), (10, 9), (7, 18), (1, 5), (2, -4)]
points = sorted(points, key=lambda point: point[0])
print(points)

print(1 % 2)

from functools import reduce 

floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59, 34.23, 12.12, 4.67, 2.45, 9.32]
words = ['racecar', 'akinremi', 'deed', 'temidayo', 'omoseun', 'civic', 'TATTARRATTAT', 'malayalam', 'nun']
numbers = [4, 6, 9, 23, 5]

# Исправьте этот код
map_result = list(map(lambda num: round(num**2, 1), floats))
filter_result = list(filter( lambda name: name if (len(list(name)) > 4) and (name == "".join(list(name)[-1::-1])) else None, words))
reduce_result = reduce(lambda num1, num2: num1 + num2, numbers, 0)
# (len(list(name)) > 4) and 
print(map_result)
print(filter_result)
print(reduce_result)
name = "privet"

print("".join(list(name)[-1::-1]))