"""
Задание 2.

Приведен код, который формирует из введенного числа
обратное по порядку входящих в него цифр.
Задача решена через рекурсию
Выполнена попытка оптимизировать решение через мемоизацию.
Сделаны замеры обеих реализаций.

Сделайте аналитику, нужна ли здесь мемоизация или нет и почему?!!!
Будьте внимательны, задание хитрое. Не все так просто, как кажется.
"""

from timeit import timeit
from random import randint


def recursive_reverse(number):
    if number == 0:
        return ''
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'


num_100 = randint(10000, 1000000)
num_1000 = randint(1000000, 10000000)
num_10000 = randint(100000000, 10000000000000)

print('Не оптимизированная функция recursive_reverse')
print(
    timeit(
        "recursive_reverse(num_100)",
        setup='from __main__ import recursive_reverse, num_100',
        number=10000))
print(
    timeit(
        "recursive_reverse(num_1000)",
        setup='from __main__ import recursive_reverse, num_1000',
        number=10000))
print(
    timeit(
        "recursive_reverse(num_10000)",
        setup='from __main__ import recursive_reverse, num_10000',
        number=10000))


def memoize(f):
    cache = {}

    def decorate(*args):

        if args in cache:
            print(f'args in cache {args}')
            return cache[args]
        else:
            cache[args] = f(*args)
            print(f'added to cache {args}')
            return cache[args]

    return decorate


@memoize
def recursive_reverse_mem(number):
    if number == 0:
        return ''
    return f'{str(number % 10)}{recursive_reverse_mem(number // 10)}'


print('Оптимизированная функция recursive_reverse_mem')
print(
    timeit(
        'recursive_reverse_mem(num_100)',
        setup='from __main__ import recursive_reverse_mem, num_100',
        number=10000))
print(
    timeit(
        'recursive_reverse_mem(num_1000)',
        setup='from __main__ import recursive_reverse_mem, num_1000',
        number=10000))
print(
    timeit(
        'recursive_reverse_mem(num_10000)',
        setup='from __main__ import recursive_reverse_mem, num_10000',
        number=10000))

"""
если дописать 
print(f'added to cache {args}') если в кэш добавляется очередной number
print(f'args in cache {args}') если number уже в кэше

при первом вызове number каждый раз разный (число при очередном углублении в рекурсию меньше на один знак),

added to cache (0,)
added to cache (1,)
added to cache (17,)
added to cache (176,)
added to cache (1763,)
added to cache (17639,)
added to cache (176390,)

поэтому кэш каждый раз по идее пополняется разными числами. то есть при единственном вызове рекурсивной функции смысла от кэша нет.

при следующем вызове этой рекурсивной функции в кэше уже хранится значение от  (176390,). то есть при больших числах повторных
вызовов функций (number=10000) кэш сразу вернет значение от самого длинного числа (первично-поданного), args будет уже в кэшэ
args in cache (176390,)
args in cache (176390,)
args in cache (176390,)
args in cache (176390,)
и так далее 10000 раз

этим можно, наверное, объяснить лучшую эффективнось работы алгоритма при многочисленных вызовах функции (number > 1)
а при единственном вызове смысла от кэша в этом алгоритме нет
"""
