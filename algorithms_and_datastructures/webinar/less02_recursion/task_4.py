"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов: 3, их сумма: 0.75

Подсказка:
Каждый очередной элемент в 2 раза меньше предыдущего и имеет противоположный знак

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""


def get_set_sum(n: int, num: float = 1):
    return num if n == 1 else num + get_set_sum(n=n - 1, num=num / - 2)


if __name__ == '__main__':
    is_complete = False

    while not is_complete:
        try:
            user_n = int(input('enter number of elements from set (1, -0.5, 0.25, -0.125 ... n) > '))
            assert user_n > 0, 'number of elements should be at least 1'

            print(f'number of set elements: {user_n}, their sum: {get_set_sum(user_n)}')
            is_complete = True
        except AssertionError as e:
            print(e)
        except Exception as e:
            print(e)
