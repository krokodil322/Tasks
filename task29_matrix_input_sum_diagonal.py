


# size_matrix = int(input())
# matrix = [[int(row) for row in input().split()] for _ in range(size_matrix)]
# print(sum([matrix[index][index] for index in range(len(matrix))]))
size_matrix = int(input())
print(sum([print(int(num)) for index in range(size_matrix) for num in input().split()[index]]))

# print([print(input().split()) for index in range(size_matrix)])