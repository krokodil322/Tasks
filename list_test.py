# zeros = [0] * 10
# print(zeros)
# print(len(zeros))

# numbers = [4, 8, 12, 16, 34, 56, 100]
# numbers[1:4] = [20, 24, 28]
# print(numbers)

# numbers = [5, 10, 15, 25]
# print(numbers[::-2])

# list1 = [[1, 7, 8], [9, 7, 102], [6, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
# maximum = -1
# maximum = max([max(item) for item in list1])

# print(maximum)

# list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
# for item in list1:
# 	item.reverse()
# print(list1)

# list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
# total = 0
# counter = 0
# for item in list1:
# 	counter += len(item)
# 	total += sum(item)
# print(total/counter)

# my_list = [[0] * 3 for item in range(0, 3)]
# print(my_list)
# list1 = [[1] * 3] * 3
# print(list1)
# list1[0][1] = 5
# print(list1)

my_list = [[12, 221, 3], [41, 5, 633], [71, 8, 99]]

maximum = my_list[0][0]
minimum = my_list[0][0]

for row in my_list:
    maximum = max(row)
    minimum = min(row)

print(maximum, minimum)

