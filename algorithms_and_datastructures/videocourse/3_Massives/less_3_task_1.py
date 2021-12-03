# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
# Примечание: 8 разных ответов.

print('in range [2, 99]:')
for n in range(2, 10):
    print(f'divisible by {n}: ', end='\t')
    count = 0

    for num in range(2, 100):
        if num % n == 0:
            count += 1
    print(count, 'numbers')