"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Оптимизируйте, чтобы снизить время выполнения
Проведите повторные замеры.

Добавьте аналитику: что вы сделали и почему!!!
Без аналитики задание не принимается
"""

import timeit
import numpy as np

ncalls = 100000


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    return [n[0] for n in enumerate(nums) if n[0] % 2 == 0]


def func_3(nums):
    intarray = np.array(nums)
    return np.where(intarray % 2 == 0)


print(f"list append implementation:\n"
      f"{round(timeit.timeit('func_1(user_nums)', number=ncalls, globals=globals()), 3)} seconds")
print(f"enumerate + list comprehension implementation:\n"
      f"{round(timeit.timeit('func_2(user_nums)', number=ncalls, globals=globals()), 3)} seconds")
print(f"numpy implementation:\n"
      f"{round(timeit.timeit('func_3(user_nums)', number=ncalls, globals=globals()), 3)} seconds")

"""
list append implementation:
13.316 seconds
enumerate + list comprehension implementation:
15.299 seconds
numpy implementation:
9.812 seconds

вывод: numpy быстрей, пишут потомучто обьекты numpy хранятся в близкой друг к другу области памяти. 
плюс пишут что numpy как то так реализован на этом волшебном С, что на него не влияют затраты самого питона на 
проверки динамического типа для каждого элемента.
(benefits from spatial locality of reference, np refers to the use of data elements within relatively close storage locations. 
Also, many Numpy operations are implemented in C, avoiding the general cost of loops in Python, pointer indirection and 
per-element dynamic type checking.)

В то время как lists, образованные хоть спомощью петель или спомощью list comprehension это массивы ссылок на обьекты 
(хоть даже если и одного типа, но при этом хранящихся в относительно отдаленных друг от друга областях памяти).
"""
