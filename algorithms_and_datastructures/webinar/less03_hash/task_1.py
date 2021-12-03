"""
Задание 1.

Реализуйте свои пользовательские функции, в которых реализуйте:

a) заполнение списка и словаря,
   сделайте замеры и сделайте выводы, что выполняется быстрее и почему
b) выполните набор операций и со списком, и со словарем,
   сделайте замеры и сделайте выводы, что и где выполняется быстрее и почему

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор для подсчета времени работы ваших пользовательских функций
И примените ее к своим функциям!

Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.
"""

import random
import time

massive_length = 1000000
from_a = -100
to_b_included = 100


def get_time(original_func):
    def wrapper_func(*args):
        t_1 = time.time()
        original_func_res = original_func(*args)
        t_2 = time.time()
        print(t_2 - t_1)
        return original_func_res

    return wrapper_func


@get_time
def get_random_list(list_len=10, a=-100, b=100):
    """
    returns list of random digits (random from a to b) length = list_len
    """
    return [random.randint(a, b + 1) for n in range(list_len)]


@get_time
def get_random_dict(dict_size=10, a=-100, b=100):
    """
    returns random dict with 'key_n: value_(random digit from a to b)' size of dict = dict_size
    """
    return {'key_' + str(n): 'value_' + str(random.randint(a, b + 1)) for n in range(dict_size)}


my_list = get_random_list(massive_length, from_a, to_b_included)
# 1.5031611919403076

my_dict = get_random_dict(massive_length, from_a, to_b_included)
# 2.118091583251953


"""
list comprehension быстрее
думаю, потомучто
в случае list comp: делает список и по очередному индексу дабавляет в список очередное значение
в случае dict comp: перед связыванием keys: values, вместо очередного индекса нужно вычислить хеш от key
"""


@get_time
def list_insert_to_last(my_list: list):
    my_list.insert(len(my_list), 1)
    return my_list


print('list insert to last:')
list_insert_to_last(my_list)


@get_time
def list_append_to_last(my_list: list):
    my_list.append(1)
    return my_list


print('list append to last:')
list_append_to_last(my_list)


@get_time
def list_insert_to_first(my_list: list):
    my_list.insert(0, 1)
    return my_list


print('list insert to first:')
list_insert_to_first(my_list)


@get_time
def list_pop_from_last(my_list: list):
    my_list.pop(len(my_list) - 1)
    return my_list


print('list pop from last:')
list_pop_from_last(my_list)


@get_time
def list_pop_from_first(my_list: list):
    my_list.pop(0)
    return my_list


print('list pop from first:')
list_pop_from_first(my_list)


@get_time
def list_copy(my_list: list):
    copy_list = my_list.copy()
    return copy_list


print('list copy:')
list_copy(my_list)


@get_time
def list_clear(my_list: list):
    my_list.clear()
    return my_list


print('list clear:')
list_clear(my_list)


@get_time
def dict_add(my_dict: dict):
    my_dict['added_key'] = 'added value'
    return my_dict


print('dict add:')
dict_add(my_dict)


@get_time
def dict_update(my_dict: dict):
    my_dict.update(updated_key='updated value')
    return my_dict


print('dict update:')
dict_update(my_dict)


@get_time
def dict_pop(my_dict: dict):
    my_dict.pop('added_key')
    return my_dict


print('dict pop:')
dict_pop(my_dict)


@get_time
def dict_pop_last(my_dict: dict):
    my_dict.popitem()
    return my_dict


print('dict pop last:')
dict_pop_last(my_dict)


@get_time
def dict_get(my_dict: dict):
    my_dict.get('key_1')
    return my_dict


print('dict get:')
dict_get(my_dict)


@get_time
def dict_copy(my_dict: dict):
    new_dict = my_dict.copy()
    return new_dict


print('dict copy:')
dict_copy(my_dict)


@get_time
def dict_clear(my_dict: dict):
    my_dict.clear()
    return my_dict


print('dict clear:')
dict_clear(my_dict)

"""
list insert to last: list.insert(len(list), 1) 
0.0
O(1)

list append to last:
0.0
O(1)

list insert to first:
0.0009984970092773438
O(n)

list pop from last:
0.0
O(1)

list pop from first:
0.0010442733764648438
O(n)


list copy:
0.004938364028930664
O(n)

list clear:
0.012964010238647461
O(n)

dict add:
0.0
O(1)

dict update:
0.0
O(1)

dict pop:
0.0
O(1)

dict pop last:
0.0
O(1)

dict get:
0.0
O(1)

dict copy:
0.03196239471435547
O(len(...))

dict clear:
0.046631574630737305
O(1)


вывод: все нотации подтверждают свою сложность кроме dict.clear
в словарях все изменения O(1) т.к. массив не по индексам, а ассоциативный (по хешам от ключей)
в ваших листовках по сложностям, кстати, d.popitem() указан что удаляет рандомно, а по документации он удаляет по LIFO 
"""
