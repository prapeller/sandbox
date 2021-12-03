"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.

Задача: 
1) создайте простой список (list) и очередь (deque). Сделайте замеры и оцените что заполняется быстрее.
2) Выполните различные операции с каждым из объектов. Сделайте замеры и оцените, где и какие операции быстрее.

Не забудьте, что сравнивать, например, можно операцию appendleft дека и insert списка и т.д.
"""

from collections import deque
import cProfile
from timeit import timeit

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# 1)

ncalls = 10000


def fill_list(num):
    my_list = []
    for i in range(num):
        my_list.append(i)
    return my_list


def fill_deque(num):
    my_deque = deque()
    for i in range(num):
        my_deque.append(i)
    return my_deque


# cProfile.run('fill_list(ncalls)')
# print(timeit('fill_list(ncalls)', globals=globals(), number=1000))
# print(timeit('fill_list(ncalls)', globals=globals(), number=10000))
# cProfile.run('fill_deque(ncalls)')
# print(timeit('fill_deque(ncalls)', globals=globals(), number=1000))
# print(timeit('fill_deque(ncalls)', globals=globals(), number=10000))
"""
fill_list:
10004 function calls in 0.004 seconds
0.8916 сек при number = 1000
8.9277 сек при number = 10000

fill_deque:
10004 function calls in 0.003 seconds
0.8644 сек при number = 1000
8.0305 сек при number = 10000

вывод: заполнение list() / deque() через .append() примерно одинаковое
"""


def fill_list_comp(num):
    return [n for n in range(num)]


def fill_deque_list_comp(num):
    return deque([n for n in range(num)])


# cProfile.run('fill_list_comp(ncalls)')
# print(timeit('fill_list_comp(ncalls)', globals=globals(), number=1000))
# print(timeit('fill_list_comp(ncalls)', globals=globals(), number=10000))
# cProfile.run('fill_deque_list_comp(ncalls)')
# print(timeit('fill_deque_list_comp(ncalls)', globals=globals(), number=1000))
# print(timeit('fill_deque_list_comp(ncalls)', globals=globals(), number=10000))

"""
fill_list_comp:
5 function calls in 0.001 seconds
0.4037 сек при number = 1000
3.6669 сек при number = 10000


fill_deque_list_comp:
5 function calls in 0.002 seconds
0.7428 сек при number = 1000
5.2432 сек при number = 10000

вывод: 
заполнение list через list comprehension быстрей раза в 2 чем через .append()
формирование deque из list, заполненный через list comprehension немного медленней чем просто list comprehension..
ну это и понятно..
"""


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# 2)


def list_insert_to_first(num):
    my_list = []
    for i in range(num):
        my_list.insert(0, i)
    return my_list


def deque_insert_to_first(num):
    my_deque = deque()
    for i in range(num):
        my_deque.appendleft(i)
    return my_deque


# cProfile.run('list_insert_to_first(ncalls)')
# print(timeit('list_insert_to_first(ncalls)', globals=globals(), number=100))
# print(timeit('list_insert_to_first(ncalls)', globals=globals(), number=1000))
# cProfile.run('deque_insert_to_first(ncalls)')
# print(timeit('deque_insert_to_first(ncalls)', globals=globals(), number=100))
# print(timeit('deque_insert_to_first(ncalls)', globals=globals(), number=1000))

"""
list_insert_to_first:
10004 function calls in 0.034 seconds
2.8040  \ number = 100
26.1571 \ number = 1000

deque_insert_to_first:
10004 function calls in 0.006 seconds
0.0761 \ number = 100
0.8102 \ number = 1000

вывод: вставка в начало списка у deque намного быстре
"""


def list_extend(num):
    my_list = [1, 2, 3]
    list_to_extend = [1, 2, 3]
    for i in range(num):
        my_list += list_to_extend
    return my_list


def deque_extend(num):
    my_list = [1, 2, 3]
    my_deque = deque(my_list)
    for i in range(num):
        my_deque.extend(my_list)
    return my_deque


# cProfile.run('list_extend(ncalls)')
# print(timeit('list_extend(ncalls)', globals=globals(), number=1000))
# print(timeit('list_extend(ncalls)', globals=globals(), number=10000))
# cProfile.run('deque_extend(ncalls)')
# print(timeit('deque_extend(ncalls)', globals=globals(), number=1000))
# print(timeit('deque_extend(ncalls)', globals=globals(), number=10000))

"""
list_extend:
4 function calls in 0.001 seconds
0.8533515 / number=1000
6.6830236 / number=10000

deque_extend:
10004 function calls in 0.004 seconds
1.4277636999999999 /number=1000
14.992272800000002 /number=10000

расширение в списке(конкатенация списков) значительно быстрей нежели deque, 
но у list нет extendleft(), которые расширяют deque примерно с такой же скоростью как и простая extend()
"""

my_list_to_pop = [n for n in range(ncalls + 1)]
my_deque_to_pop = deque(my_list_to_pop)


def list_pop(num):
    return my_list_to_pop.pop()


def deque_pop(num):
    my_deque_to_pop.pop()
    return my_deque_to_pop


# cProfile.run('list_pop(ncalls)')
# print(timeit('list_pop(ncalls)', globals=globals(), number=10000))
# cProfile.run('deque_pop(ncalls)')
# print(timeit('deque_pop(ncalls)', globals=globals(), number=10000))

"""
list_pop:
5 function calls in 0.000 seconds
0.0015313999999999883 / number=10000

5 function calls in 0.000 seconds
0.001509300000000019 / number=10000

вывод:
выдергивает последний элемент примерно с одной и той же скоростью
"""

my_list_to_pop_first = [n for n in range(ncalls + 1)]
my_deque_to_pop_first = deque(my_list_to_pop_first)


def list_pop_first():
    return my_list_to_pop_first.pop(0)


def deque_pop_first():
    return my_deque_to_pop_first.popleft()


cProfile.run('list_pop_first()')
print(timeit('list_pop_first()', globals=globals(), number=10000))
cProfile.run('deque_pop_first()')
print(timeit('deque_pop_first()', globals=globals(), number=10000))

my_list = [n for n in range(ncalls)]
my_deque = deque(my_list_to_pop)


def list_reverse(num):
    return my_list.reverse()


def deque_reverse(num):
    return my_deque.reverse()


# cProfile.run('list_reverse(ncalls)')
# print(timeit('list_reverse(ncalls)', globals=globals(), number=100000))
# print(timeit('list_reverse(ncalls)', globals=globals(), number=1000000))
# cProfile.run('deque_reverse(ncalls)')
# print(timeit('deque_reverse(ncalls)', globals=globals(), number=100000))
# print(timeit('deque_reverse(ncalls)', globals=globals(), number=1000000))

"""
5 function calls in 0.000 seconds
0.5951 /  number=100000
5.8170 /  number=1000000

5 function calls in 0.000 seconds
1.3870 /  number=100000
14.1216 / number=1000000

вывод: list разворачивается значительно быстрей
"""

"""
общий вывод:
deque особо не интересен, кроме как если нужно встроенное ограничение количесва элементов в списке (maxlen=...)
или если нужно встроенная функция перемещения некоторого количества элементов с конца в начало .rotate()
в остальном эффективность deque либо такая же как у list, либо ниже
"""