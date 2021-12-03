# 7. Написать программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется
# равенство: 1+2+...+n = n(n+1)/2, где n — любое натуральное число.

# draw.io diagram:
# https://drive.google.com/file/d/1vBqh4C1H5pclFo49cmuYPrjYHIyoKqQ-/view?usp=sharing

n = int(input('enter number for calculating 1+2+...+n: '))
left_part = 0
for i in range(n + 1):
    left_part += i
right_part = n * (n + 1) / 2
print(f'1+2+...+n = n(n+1)/2 ? {left_part == right_part}')