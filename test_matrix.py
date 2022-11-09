# matrix = [
# 			[11, 12, 13],
# 			[21, 22, 23],
# 			[31, 32, 33]
# 		 ]

# print(matrix[2][2])

# for row_index in range(len(matrix)):
# 	for column_index in range(len(matrix[0])):
# 		print(matrix[row_index][column_index], end=" ")
# 	print()

# matrix  = [[277, -930, 11, 0],
#            [9, 43, 6, 87],
#            [4456, 8, 290, 7]]

# for row_index in range(len(matrix)):
# 	for column_index in range(len(matrix[0])):
# 		print(str(matrix[row_index][column_index]).rjust(4), end=" ")
# 	print()

# matrix = [[0]*8 for _ in range(8)]
# n = len(matrix)

# for i in range(len(matrix)):
# 	for j in range(len(matrix[0])):
# 		matrix[i][i] = 1
# 		matrix[i][n - i - 1] = 2
	
# for item in matrix:
# 	print(item)


n = 5
a = [[19, 21, 33, 78, 99], 
     [41, 53, 66, 98, 76], 
     [79, 80, 90, 60, 20],
     [33, 11, 45, 67, 90],
     [45, 67, 12, 98, 23]]

maximum = -1
minimum = 100

for i in range(n):
    if a[i][i] > maximum:
        maximum = a[i][i]
    if a[i][n - i - 1] < minimum:
        minimum = a[i][n - i - 1]
print(maximum)
print(minimum)
print(minimum + maximum)