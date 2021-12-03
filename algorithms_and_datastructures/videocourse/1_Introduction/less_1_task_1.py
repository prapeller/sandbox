# 1. Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6.
# Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака.

# draw.io diagram:
# https://drive.google.com/file/d/1Bpd6LTEg-jYVBi_hjwJZFQPKg7GJVipY/view?usp=sharing

num_1 = 5
num_2 = 6

print(f'{num_1} = {bin(num_1)}')
print(f'{num_2} = {bin(num_2)}')
print(f'~ {bin(num_1)} = {bin(~num_1)}')
print(f'~ {bin(num_2)} = {bin(~num_2)}')
print(f'{bin(num_1)} | {bin(~num_1)} = {bin(num_1 | num_2)}')
print(f'{bin(num_1)} & {bin(~num_1)} = {bin(num_1 & num_2)}')
print(f'{bin(num_1)} ^ {bin(~num_1)} = {bin(num_1 ^ num_2)}')
print(f'bitwise right shift of {bin(num_1)} = {bin(num_1 >> 2)}')
print(f'bitwise left shift of {bin(num_1)} = {bin(num_1 << 2)}')
