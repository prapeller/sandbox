# задание из урока 3 задание 9.
# Найти максимальный элемент среди минимальных элементов столбцов матрицы.



import random
import sys
import tracemalloc


# 1)(перебор по столбцам)
def max_of_columns_mins_1(size):
    matrix = []
    for i in range(size):
        matrix.append([])
        for j in range(size):
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

    return max_of_min


# 2)(list comprehension)
def max_of_columns_mins_2(size):
    matrix = [[random.randint(-50, 50) for _ in range(size)] for _ in range(size)]
    matrix = list(zip(*matrix))
    min_col_list = [min(matrix[i]) for i in range(len(matrix))]
    max_of_min = max(min_col_list)

    return max_of_min


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# как обычно странное задание. сами выберите непонять че, проанализируйте непонять че,
# размер памяти выделяемый под переменные... не понял как анализ отдельных переменных может помочь в том случае,
# когда у вас написан какойто скрипт и вам нужно понять сколько памяти выделилось для
# реализации этого скрипта.. поэтому
# проявил творчество и фантазию и использовал уже существующую стандартную библиотеку для отслеживания утечки памяти

tracemalloc.start()

max_of_columns_mins_1(10)
print("max_of_columns_mins_1: Current: %d, Peak %d" % tracemalloc.get_traced_memory())
tracemalloc.clear_traces()

max_of_columns_mins_2(10)
print("max_of_columns_mins_2: Current: %d, Peak %d" % tracemalloc.get_traced_memory())
tracemalloc.clear_traces()

tracemalloc.stop()


# в моем случае
# print(sys.version, sys.platform, sep='\n')
# 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# показатели следующие:

# max_of_columns_mins_1: Current: 1008, Peak 4000
# max_of_columns_mins_2: Current: 3296, Peak 6204

# вывод: list comprehensions прилично нагружают память по сравнению с обычными циклами...
