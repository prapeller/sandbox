"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.

Без аналитики задание считается не принятым!
"""

import timeit
import cProfile
import numpy as np
from collections import Counter

ncalls = 1000000

array = [1, 3, 1, 3, 4, 5, 1]
ndarray = np.array(array)


def func_1():
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


def func_3():
    counter = Counter(array)
    elem_4, max_4 = counter.most_common(1)[0]
    return f'Чаще всего встречается число {elem_4}, ' \
           f'оно появилось в массиве {max_4} раз(а)'


def func_4():
    elem_5 = max(set(array), key=array.count)
    max_5 = array.count(elem_5)
    return f'Чаще всего встречается число {elem_5}, ' \
           f'оно появилось в массиве {max_5} раз(а)'



cProfile.run('print(func_1())')
print(timeit.timeit('func_1()', globals=globals(), number=ncalls))

"""
1) # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 


Чаще всего встречается число 1, оно появилось в массиве 3 раз(а)
         12 function calls in 0.001 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.001    0.001 <string>:1(<module>)
        1    0.001    0.001    0.001    0.001 task_4.py:26(func_1)
        1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        7    0.000    0.000    0.000    0.000 {method 'count' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


2.0024122
O(n^2)

"""

cProfile.run('print(func_2())')
print(timeit.timeit('func_2()', globals=globals(), number=ncalls))

"""
2) # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

Чаще всего встречается число 1, оно появилось в массиве 3 раз(а)
         21 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 task_4.py:38(func_2)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.max}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        7    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        7    0.000    0.000    0.000    0.000 {method 'count' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}


2.7594013000000004
O(n^2)
"""


cProfile.run('print(func_3())')
print(timeit.timeit('func_3()', globals=globals(), number=ncalls))

"""
3) # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

Чаще всего встречается число 1, оно появилось в массиве 3 раз(а)
         40 function calls (26 primitive calls) in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 __init__.py:581(__init__)
        1    0.000    0.000    0.000    0.000 __init__.py:600(most_common)
        1    0.000    0.000    0.000    0.000 __init__.py:649(update)
        8    0.000    0.000    0.000    0.000 _collections_abc.py:405(__subclasshook__)
      8/1    0.000    0.000    0.000    0.000 abc.py:100(__subclasscheck__)
        1    0.000    0.000    0.000    0.000 abc.py:96(__instancecheck__)
        1    0.000    0.000    0.000    0.000 heapq.py:521(nlargest)
        1    0.000    0.000    0.000    0.000 task_4.py:54(func_4)
        1    0.000    0.000    0.000    0.000 {built-in method _abc._abc_instancecheck}
      8/1    0.000    0.000    0.000    0.000 {built-in method _abc._abc_subclasscheck}
        1    0.000    0.000    0.000    0.000 {built-in method _collections._count_elements}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.isinstance}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.iter}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.max}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}


4.7609294
"""

cProfile.run('print(func_4())')
print(timeit.timeit('func_4()', globals=globals(), number=ncalls))

"""
4) # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

Чаще всего встречается число 1, оно появилось в массиве 3 раз(а)
         7 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 task_4.py:61(func_5)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.max}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        1    0.000    0.000    0.000    0.000 {method 'count' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


1.9681093999999995
"""

"""
вывод: 
первые два предложенных алгорихотма O(n^2),
третий написанный возможно и О(n), но возможно Counter отнимает слишком много времени
как выяснилось самое быстрое - это 4й, через max(set(list), key=list.count) а потом list.count для подсчета кол-ва

думаю count более оптимизирован.. хз)) 

"""

