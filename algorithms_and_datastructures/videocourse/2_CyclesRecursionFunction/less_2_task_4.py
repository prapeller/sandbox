# Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… Количество элементов (n) вводится с клавиатуры.
# draw.io diagram:
# https://drive.google.com/file/d/1tPHv6xrySCWpzfBJSiayYftKB5esfyEX/view?usp=sharing

n = int(input('enter number of numbers in sequence 1, -0.5, 0.25, -0.125, ... '))
next = 1
result = 0
for _ in range(n):
    result += next
    next *= -0.5
print(f'sum of sequence: {result}')