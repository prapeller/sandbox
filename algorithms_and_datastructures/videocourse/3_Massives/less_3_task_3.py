# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

rand_list = [random.randint(-100, 100) for _ in range(10)]
print(f'before: {rand_list}')

max_n = float('-inf')
max_n_i = 0

min_n = float('inf')
min_n_i = 0


for i in range(len(rand_list)):
    if rand_list[i] > max_n:
        max_n = rand_list[i]
        max_n_i = i

    if rand_list[i] < min_n:
        min_n = rand_list[i]
        min_n_i = i

print(f'max: {max_n}[{max_n_i}], min: {min_n}[{min_n_i}]')

rand_list[max_n_i] = min_n
rand_list[min_n_i] = max_n

print(f'after: {rand_list}')
