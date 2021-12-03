"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""

from collections import OrderedDict
from timeit import timeit
import cProfile

# заполнение

ncalls = 1000


def fill_dict(num):
    my_dict = {}
    for i in range(num):
        my_dict[str(i)] = i
    return my_dict


def fill_ordered_dict(num):
    my_ordered = OrderedDict({})
    for i in range(num):
        my_ordered[str(i)] = i
    return my_ordered


# cProfile.run('fill_dict(ncalls)')
# print(timeit('fill_dict(ncalls)', globals=globals(), number=1000))
# print(timeit('fill_dict(ncalls)', globals=globals(), number=10000))
# cProfile.run('fill_ordered_dict(ncalls)')
# print(timeit('fill_ordered_dict(ncalls)', globals=globals(), number=1000))
# print(timeit('fill_ordered_dict(ncalls)', globals=globals(), number=10000))

"""
4 function calls in 0.001 seconds
0.4429448 \ number=1000
3.4624888 \ number=10000
         
4 function calls in 0.001 seconds
0.4177363 \ number=1000
4.2308472 \ number=1000

вывод: заполнение примерно одинаковое по скорости
"""


# получение

filled_dict = fill_dict(ncalls)
filled_ordered = fill_ordered_dict(ncalls)


def get_from_dict(num):
    for i in range(num):
        a = filled_dict.get(i)


def get_from_ordered(num):
    for i in range(num):
        a = filled_ordered.get(i)


# cProfile.run('get_from_dict(ncalls)')
# print(timeit('get_from_dict(ncalls)', globals=globals(), number=10000))
# print(timeit('get_from_dict(ncalls)', globals=globals(), number=100000))
# cProfile.run('get_from_ordered(ncalls)')
# print(timeit('get_from_ordered(ncalls)', globals=globals(), number=10000))
# print(timeit('get_from_ordered(ncalls)', globals=globals(), number=100000))

"""
1004 function calls in 0.000 seconds
1.1156 \ number=10000
10.6507 \ number=100000

1004 function calls in 0.000 seconds
1.0907 \ number=10000
10.5872 \ number=100000

вывод: и получение примрено одинаковое по скорости
"""

# a = {'cat': 5, 'mouse': 4, 'dog': 2}
# b = {'mouse': 4, 'cat': 5, 'dog': 2}
# sorted_by_key = sorted(a.items(), key=lambda x: x[0])
# sorted_by_value = sorted(a.items(), key=lambda x: x[1])
# print(a == b) # True
# print(sorted_by_key == sorted_by_value) # False
# print()
#
# ordered_a = OrderedDict(a)
# ordered_b = OrderedDict(b)
# print(ordered_a == ordered_b) # False
# print()
#
# ordered = OrderedDict(a)
# print(ordered)
# ordered.move_to_end('mouse', last=False)
# print(ordered)
# ordered.move_to_end('mouse', last=True)
# print(ordered)
# print()
#
# # замеры
# a['cow'] = 1
# print(a)
# ordered['cow'] = 1
# print(ordered)
# ordered['cat'] = 1
# print(ordered)
# print()
#
#
# abd_dict = {'a': 5, 'b': 4, 'c': 3, 'd': 2, 'e': 1}
#
# sorted_by_key_length_list = sorted(abd_dict.items())
# print(sorted_by_key_length_list)
# sorted_by_value_list = sorted(abd_dict.items(), key=lambda x: x[1])
# print(sorted_by_value_list)
#
# reversed_list = reversed(sorted_by_key_length_list)
# print(list(reversed_list))
#
# ordered_by_value_dict = OrderedDict(sorted(abd_dict.items(), key=lambda x: x[1]))
# print(ordered_by_value_dict)
# ordered_by_value_dict['f'] = 6
# print(ordered_by_value_dict)
# ordered_by_value_dict['1'] = 0
# print(ordered_by_value_dict)
# ordered_by_value_dict.move_to_end('1', last=False)
# print(ordered_by_value_dict)

"""
вывод: наверное имеет смысл использовать OrderedDict там, где важно сохранять и соблюдать порядок всего словаря
 по ключу или значению, чтобы работать с крайними items по принципу очереди
"""