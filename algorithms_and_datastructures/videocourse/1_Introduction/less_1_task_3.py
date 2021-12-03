# 3. Написать программу, которая генерирует в указанных пользователем границах:
# a. случайное целое число,
# b. случайное вещественное число,
# c. случайный символ.

# a, b, c diagram at different lists of draw.io:
# https://drive.google.com/file/d/14kQ9UQs1qpPZKz3DW39ftIFfNj3sHJQ4/view?usp=sharing


import random

# a)
x = int(input('enter the smallest range integer x... '))
y = int(input('enter the largest range integer y... '))
z = random.randint(x, y)
print(z)

# b)
x = float(input('enter the smallest range nubmer x... '))
y = float(input('enter the largest range number y... '))
z = random.uniform(x, y)
print(z)

# c)
start_chr = input('enter starting character... ').lower()
start_num = ord(start_chr)
finish_chr = input('enter finishing character... ').lower()
finish_num = ord(finish_chr)
rand_char = chr(random.randint(start_num, finish_num))
print(rand_char)