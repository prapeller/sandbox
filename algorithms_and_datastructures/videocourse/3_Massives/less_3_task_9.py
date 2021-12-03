# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import random

matrix = []
for i in range(4):
    matrix.append([])
    for j in range(5):
        matrix[i].append(random.randint(-50, 50))

min_col_list = []

for j in range(len(matrix[0])):
    min_col = float('inf')
    for i in range(len(matrix)):
        if matrix[i][j] < min_col:
            min_col = matrix[i][j]
    min_col_list.append(min_col)

max_of_min = float('-inf')
for n in min_col_list:
    if n > max_of_min:
        max_of_min = n

for line in matrix:
    for n in line:
        print(f'{n:>5}', end='')
    print()

print(f'\nminimal elements of columns: \n{min_col_list}\n')
print(f'maximal of them: {max_of_min}')
