# 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр. Вывести на экран это число и сумму
# его цифр.

# draw.io diagram:
# https://drive.google.com/file/d/1sL76Th6uXiWgIiZGvj9iO8EqVFSDxpfa/view?usp=sharing

qty = int(input('enter quantity of integers you put for comparing: '))
max_integer = ''
max_count = 0

for _ in range(qty):
    integer = input('enter integer: ')
    count = 0

    for n in integer:
        count += int(n)

    if count > max_count:
        max_integer = integer
        max_count = count

print(f'max integer: {max_integer}, sum of its digits: {max_count}')

