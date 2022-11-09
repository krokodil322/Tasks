import random

# print(random.randint(0, 10))

# print(random.randrange(7, 10))

# mylist = list(range(0, 10, 2))
# print(mylist)

# for _ in range(20):
# 	print(random.random(), end= "|")
# print()
# print(random.uniform(1.7, 19.28))

# random.seed(17)   # явно устанавливаем начальное значение для генератора случайных чисел
# for _ in range(10):
#     print(random.randint(1, 100), end="|")

# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# print(random.shuffle(numbers))
# print(numbers)

mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(random.choice(mylist))

print(random.sample([1, 2, 3, 4, 5, 6, 7, 8, 9], 4))
