# 7. В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой
# (оба минимальны), так и различаться.

import random

rand_list = [random.randint(0, 5) for n in range(5)]
print(rand_list)

first_min = float('inf')
second_min = float('inf')

for i in range(len(rand_list)):
    if rand_list[i] < first_min:
        first_min = rand_list[i]

min_index_list = []

for i in range(len(rand_list)):
    if rand_list[i] == first_min:
        min_index_list.append(i)

if len(min_index_list) > 1:
    second_min = rand_list[min_index_list[1]]
else:
    for i in range(len(rand_list)):
        if first_min < rand_list[i] < second_min:
            second_min = rand_list[i]

print(first_min, second_min)
