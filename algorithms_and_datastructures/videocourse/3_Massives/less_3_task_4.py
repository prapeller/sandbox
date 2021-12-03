# 4. Определить, какое число в массиве встречается чаще всего.

import random

rand_list = [random.randint(0, 5) for _ in range(10)]
print(rand_list)
count_dict = {}

for i in range(len(rand_list)):
    max_freq_i = 0

    for j in range(len(rand_list)):
        if rand_list[i] == rand_list[j]:
            max_freq_i += 1

    count_dict[rand_list[i]] = max_freq_i

max_key = 0
max_value = 0
for key, value in count_dict.items():
    if value > max_value:
        max_value = value
        max_key = key

print(f'in the list above the most frequent number is: {max_key}')
