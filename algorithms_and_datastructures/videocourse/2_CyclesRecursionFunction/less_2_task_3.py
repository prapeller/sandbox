# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран. Например,
# если введено число 3486, надо вывести 6843.

# draw.io diagram:
# https://drive.google.com/file/d/1opKzvVW8GCXBr2K2fHFWpN1I3ntqwsrt/view?usp=sharing

num_str = input('enter any integer: ')
result = ''
for n in num_str:
    result = n + result
print(result)