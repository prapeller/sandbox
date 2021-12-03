# 2. Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560, в нем 3
# четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

#draw.io diagram:
# https://drive.google.com/file/d/1JPHNaFR9dln0yD7nMVimxmlTG20Pi4_z/view?usp=sharing

count_even = 0
count_odd = 0
num_str = input('enter positive integer')
for num in num_str:
    if int(num) % 2 == 0:
        count_even += 1
    else:
        count_odd += 1
print(f'even numbers: {count_even}')
print(f'odd numbers: {count_odd}')