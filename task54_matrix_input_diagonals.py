
size = [int(item) for item in input().split()]
matrix = [[0 for _ in range(size[1])] for _ in range(size[0])]
sequence = 1
#КОЛ-ВО ИТЕРАЦИЙ ЗАВИСИТ ОТ КОЛ-ВА ДИАГОНАЛЕЙ
#НАЙТИ ЧИСЛО ДИАГОНАЛЕЙ Ф-А: all_column + all_row - 1
for i in range(size[1] + size[0] - 1):
    #ИДЁМ ПО СТРОКАМ
    print(f"I:{i}")
    for j in range(size[0]):
        #ЕСЛИ ИНДЕКС СТОЛБЦА БОЛЬШЕ - 1 И
        #МЕНЬШЕ МАКСИМАЛЬНОГО ИНДЕКСА СТОЛБЦА
        print(f"\tJ:{j}")
        if ((i-j) > -1) and ((i-j) < size[1]):
            matrix[j][i-j]+=sequence
            sequence+=1
 

for row_index in range(len(matrix)):
    for column_index in range(len(matrix[0])):
        print(str(matrix[row_index][column_index]).ljust(3), end=" ")
    print()