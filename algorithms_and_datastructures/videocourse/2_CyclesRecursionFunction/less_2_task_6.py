# 6. В программе генерируется случайное целое число от 0 до 100. Пользователь должен его отгадать не более чем за 10
# попыток. После каждой неудачной попытки должно сообщаться, больше или меньше введенное пользователем число, чем то,
# что загадано. Если за 10 попыток число не отгадано, вывести ответ.

# draw.io diagram:
# https://drive.google.com/file/d/1je1ZKuFEQGuurVG4C_AX_0VunmRbiBPA/view?usp=sharing

import random

rand_num = random.randint(0, 100)
tries_count = 0

while True:
    tries_count += 1

    if tries_count > 10:
        print('game over')
        break

    print(f'tries left: {11 - tries_count}')
    user_num = int(input('enter the hidden integer from 0 to 100: '))

    if user_num > rand_num:
        print('your number is more then hidden one')
    elif user_num < rand_num:
        print('your number is less then hidden one')
    else:
        print('you are right!')
        break
