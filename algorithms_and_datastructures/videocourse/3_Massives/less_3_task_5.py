# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

import random

rand_list = [random.randint(-20, 10) for _ in range(10)]
print(rand_list)

max_neg_num = float('-inf')
max_neg_num_ind = 0

for i in range(len(rand_list)):
    if max_neg_num < rand_list[i] < 0:
        max_neg_num = rand_list[i]
        max_neg_num_ind = i

print(f'maximum negative integer in the list above: {max_neg_num}, its index {max_neg_num_ind}')
