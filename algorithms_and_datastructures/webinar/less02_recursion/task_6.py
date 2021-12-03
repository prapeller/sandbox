"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Подсказка:
Базовый случай здесь - угадали число или закончились попытки

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""

from random import randint

random_number = randint(0, 101)
print(random_number)


def guess_with_trials(n=10):
    try:
        if n == 0:
            print(f'game over, trials expired, number was {random_number}')
            return

        user_number = int(input('guess number from 0 to 100'))

        if user_number == random_number:
            print('congratulations! you won!')
            return

        if user_number < random_number:
            print('your number is less')

        elif user_number > random_number:
            print('your number is more')

        n -= 1

        return guess_with_trials(n)

    except Exception as e:
        print(e)
        return guess_with_trials(n)


if __name__ == '__main__':
    guess_with_trials()
