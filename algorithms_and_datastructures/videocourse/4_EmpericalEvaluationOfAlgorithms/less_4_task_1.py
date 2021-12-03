# задание из урока 3 задание 9.
# Найти максимальный элемент среди минимальных элементов столбцов матрицы.
# Анализируем реализации кода и временную сложность алгоритмов в зависимости от размера матрицы


import random


# 1)
def max_of_columns_mins_1(size):
    """
    1)создает матрицу размером size x size
    2)формирует список минимальных значений из каждого столбца матрицы (перебор по столбцам)
    3)находит максимальное значение из этого списка
    4)пункт о том, что саму матрицу нужно вывести - опущен (закомментирован)
    """

    # 1
    matrix = []
    for i in range(size):
        matrix.append([])
        for j in range(size):
            matrix[i].append(random.randint(-50, 50))

    # 2
    min_col_list = []

    for j in range(len(matrix[0])):
        min_col = float('inf')
        for i in range(len(matrix)):
            if matrix[i][j] < min_col:
                min_col = matrix[i][j]
        min_col_list.append(min_col)

    # 3
    max_of_min = float('-inf')
    for n in min_col_list:
        if n > max_of_min:
            max_of_min = n

    # 4
    # for line in matrix:
    #     for n in line:
    #         print(f'{n:>5}', end='')
    #     print()

    # print(f'\nminimal elements of columns: \n{min_col_list}\n')
    # print(f'maximal of them: {max_of_min}')
    return max_of_min


# 2)
def max_of_columns_mins_2(size):
    """
    1)создает матрицу размером size x size
    2)формирует список минимальных значений из каждого столбца матрицы (переворот матрицы и перебор по строкам)
    3)находит максимальное значение из этого списка

    """

    # 1
    matrix = []
    for i in range(size):
        matrix.append([])
        for j in range(size):
            matrix[i].append(random.randint(-50, 50))

    # 2
    min_col_list = []
    matrix = list(zip(*matrix))
    for i in range(len(matrix)):
        min_col = float('inf')
        for j in range(len(matrix[0])):
            if matrix[i][j] < min_col:
                min_col = matrix[i][j]
        min_col_list.append(min_col)

    # 3
    max_of_min = float('-inf')
    for n in min_col_list:
        if n > max_of_min:
            max_of_min = n

    return max_of_min


# 3)
def max_of_columns_mins_3(size):
    """
    1)создает матрицу размером size x size (list comprehension)
    2)формирует список минимальных значений из каждого столбца матрицы (перебор по столбцам, библиотечкая функция min())
    3)находит максимальное значение из этого списка(библиотечная функция max) (list comprehension + min()
    """

    # 1
    matrix = [[random.randint(-50, 50) for _ in range(size)] for _ in range(size)]

    # 2
    matrix = list(zip(*matrix))
    min_col_list = [min(matrix[i]) for i in range(len(matrix))]

    # 3
    max_of_min = max(min_col_list)

    return max_of_min

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# 1

# "less_4_task_1.max_of_columns_mins_1(10)"
# 662 function calls in 0.002 seconds
# 1000 loops, best of 5: 156 usec per loop

# "less_4_task_1.max_of_columns_mins_1(20)"
# 2578 function calls in 0.002 seconds
# 1000 loops, best of 5: 633 usec per loop

# "less_4_task_1.max_of_columns_mins_1(30)"
# 5741 function calls in 0.006 seconds
# 1000 loops, best of 5: 1.46 msec per loop

# "less_4_task_1.max_of_columns_mins_1(40)"
# 10120 function calls in 0.010 seconds
# 1000 loops, best of 5: 2.47 msec per loop

# "less_4_task_1.max_of_columns_mins_1(50)"
# 15794 function calls in 0.014 seconds
# 1000 loops, best of 5: 3.51 msec per loop

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# 2

# "less_4_task_1.max_of_columns_mins_2(10)"
# 654 function calls in 0.001 seconds
# 1000 loops, best of 5: 174 usec per loop

# "less_4_task_1.max_of_columns_mins_2(20)"
# 2544 function calls in 0.003 seconds
# 1000 loops, best of 5: 621 usec per loop

# "less_4_task_1.max_of_columns_mins_2(30)"
# 5750 function calls in 0.006 seconds
# 1000 loops, best of 5: 1.37 msec per loop

# "less_4_task_1.max_of_columns_mins_2(40)"
# 10143 function calls in 0.008 seconds
# 1000 loops, best of 5: 2.43 msec per loop

# "less_4_task_1.max_of_columns_mins_2(50)"
# 15776 function calls in 0.013 seconds
# 1000 loops, best of 5: 3.87 msec per loop

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# 3

# "less_4_task_1.max_of_columns_mins_3(10)"
# 546 function calls in 0.000 seconds
# 1000 loops, best of 5: 133 usec per loop

# "less_4_task_1.max_of_columns_mins_3(20)"
# 2131 function calls in 0.001 seconds
# 1000 loops, best of 5: 577 usec per loop

# "less_4_task_1.max_of_columns_mins_3(30)"
# 4745 function calls in 0.002 seconds
# 1000 loops, best of 5: 1.33 msec per loop

# "less_4_task_1.max_of_columns_mins_3(40)"
# 8487 function calls in 0.004 seconds
# 1000 loops, best of 5: 2.34 msec per loop

# "less_4_task_1.max_of_columns_mins_3(50)"
# 13196 function calls in 0.006 seconds
# 1000 loops, best of 5: 3.47 msec per loop


# вывод - во всех трех реализациях
# временная сложность алгоритма примерно одна и та же O(n^2) (О от n в квадрате), потомучто матрица двумерная
# но в 3м случае когда пишем по питоновски - код компактней и более читаем...
