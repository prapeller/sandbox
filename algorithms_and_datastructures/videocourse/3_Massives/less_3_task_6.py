# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. Сами
# минимальный и максимальный элементы в сумму не включать.

import random

rand_list = [random.randint(-100, 100) for n in range(10)]
print(rand_list)

maximal = float('-inf')
minimal = float('inf')

for n in rand_list:
    if n > maximal:
        maximal = n
    if n < minimal:
        minimal = n

left_ind = 0
for i in range(len(rand_list)):
    if rand_list[i] == minimal or rand_list[i] == maximal:
        left_ind = i
        break

right_ind = len(rand_list) - 1
for i in range(len(rand_list)):
    if rand_list[i] == minimal or rand_list[i] == maximal:
        right_ind = i

result_sum = 0
for i in range(left_ind + 1, right_ind):
    result_sum += rand_list[i]

print(f'in the list above maximal element: {maximal}, minimal element: {minimal}')
print(f'their indexes are {left_ind} and {right_ind}')
print(f'sum of elements between them (not inclusive): {result_sum}')
