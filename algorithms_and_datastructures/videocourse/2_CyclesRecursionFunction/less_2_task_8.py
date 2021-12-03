# 8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел. Количество вводимых
# чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.

# draw.io diagram:
# https://drive.google.com/file/d/1NY0GaFxtfy-mdUPRHzkACLiaRK4KKlg1/view?usp=sharing

qty = int(input("enter quantity of integers you'll put in sequence: "))
num = input('enter number to search in sequence: ')
sequence = ''

count = 0

for _ in range(qty):
    curr_int = input('enter integer to put in sequence for searching: ')
    sequence += curr_int

for num_seq in sequence:
    if num == num_seq:
        count += 1

print(f'found {count} matches')