
size = int(input())
matrix = [[0 for _ in range(size)] for _ in range(size)]
sequence = 1
#КОЛ-ВО ИТЕРАЦИЙ ЗАВИСИТ ОТ КОЛ-ВА ДИАГОНАЛЕЙ
#НАЙТИ ЧИСЛО ДИАГОНАЛЕЙ Ф-А: all_column + all_row - 1
x = 4
y = 4
for i in range(size * 2 - 1):
    #ИДЁМ ПО СТРОКАМ
    print(f"I:{i}")
    for j in range(size):
        #ЕСЛИ ИНДЕКС СТОЛБЦА БОЛЬШЕ - 1 И
        #МЕНЬШЕ МАКСИМАЛЬНОГО ИНДЕКСА СТОЛБЦА
        print(f"\tJ:{j}")
        if ((i-j) > -1) and ((i-j) < size) and i == (8 - x) + y - 1:
            matrix[j][i-j] = "*"
            
 

for row_index in range(len(matrix)):
    for column_index in range(len(matrix[0])):
        print(str(matrix[row_index][column_index]).ljust(3), end=" ")
    print()