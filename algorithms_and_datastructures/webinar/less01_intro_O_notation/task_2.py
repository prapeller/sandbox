"""
Задание 2.

Реализуйте два алгоритма.

Первый, в виде функции, должен обеспечивать поиск минимального значения для списка.
В основе алгоритма должно быть сравнение каждого числа со всеми другими элементами списка.
Сложность такого алгоритма: O(n^2) - квадратичная.

Второй, в виде функции, должен обеспечивать поиск минимального значения для списка.
Сложность такого алгоритма: O(n) - линейная.

Не забудьте указать сложность каждого из двух алгоритмов. Для лучшего закрепления темы
можете определить и указать сложность еще и у каждого выражения этих двух алгоритмов.

Примечание:
Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.
"""

from random import randrange
import cProfile


rand_lst = [randrange(-100, 100) for n in range(10)]

print(f'random list:\n'
      f'{rand_lst}')


# 1) O(1) + O(n) * O(n) + O(1) = O(n^2)'
def get_min_1(lst):
    min_lst = lst[0]                # O(1)
    for n in lst:                   # O(n)
        if n is min(lst):           # O(n)
            min_lst = n             # O(1)
    return min_lst                  # O(1)


# 2) O(1) + O(n) + O(1) + O(1) = O(n)'
def get_min_2(lst):
    min_lst = float('inf')          # O(1)
    for n in lst:                   # O(n)
        if n < min_lst:             # O(1)
            min_lst = n             # O(1)
    return min_lst                  # O(1)


print(f'minimal value from list by get_min_1(): {get_min_1(rand_lst)}')
cProfile.run('get_min_1(rand_lst)')


print(f'min my get_min_2(rand_lst): {get_min_2(rand_lst)}')
cProfile.run('get_min_2(rand_lst)')
