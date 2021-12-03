import copy
import gc
import random

from memory_profiler import memory_usage
from memory_profiler import profile
from timeit import default_timer
from pympler import asizeof


def profile_time_memory(func):
    def wrap(*args, **kwargs):
        m_1 = memory_usage()
        time_1 = default_timer()
        func(*args, **kwargs)
        m_2 = memory_usage()
        time_2 = default_timer()
        print(f'memory diff: {m_2[0] - m_1[0]}')
        print(f'time diff: {time_2 - time_1}')

    return wrap


"""
основы урок 7, з.1
"""

class Matrix:
    def __init__(self, matrix: list):
        self.matrix = matrix
        self.current = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.current += 1
        if self.current < len(self.matrix):
            return self.matrix[self.current]
        else:
            raise StopIteration

    def __getitem__(self, index):
        return self.matrix[index]

    def __len__(self):
        return len(self.matrix)

    def __str__(self):
        result = ''
        for line in self.matrix:
            for num in line:
                result += '{:>6}'.format(num)
            result += '\n'
        return result

    def __add__(self, other):
        sum_list = list()
        for i in range(len(self)):
            tmp_list = [sum(tup) for tup in zip(self[i], other[i])]
            sum_list.append(tmp_list)
        return Matrix(sum_list)


# @profile
# @profile_time_memory
def run():
    m_1 = Matrix([
        [random.randint(0, 1000) for n in range(10000)],
        [random.randint(0, 1000) for n in range(10000)],
        [random.randint(0, 1000) for n in range(10000)],
    ])

    m_2 = Matrix([
        [random.randint(0, 1000) for n in range(10000)],
        [random.randint(0, 1000) for n in range(10000)],
        [random.randint(0, 1000) for n in range(10000)],
    ])

    m_3 = m_1 + m_2


# run()

"""
рез-ты работы @profile:

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    64     40.8 MiB     40.8 MiB           1   @profile
    65                                         def run():
    66     41.9 MiB      0.0 MiB           2       m_1 = Matrix([
    67     41.2 MiB      0.4 MiB       10003           [random.randint(0, 1000) for n in range(10000)],
    68     41.5 MiB      0.3 MiB       10003           [random.randint(0, 1000) for n in range(10000)],
    69     41.9 MiB      0.3 MiB       10003           [random.randint(0, 1000) for n in range(10000)],
    70                                             ])
обьявили m_1, выделили 1 MiB
print(asizeof.asizeof(m_1))
# 976088

  
    72     42.8 MiB      0.0 MiB           2       m_2 = Matrix([
    73     42.1 MiB      0.2 MiB       10003           [random.randint(0, 1000) for n in range(10000)],
    74     42.5 MiB      0.4 MiB       10003           [random.randint(0, 1000) for n in range(10000)],
    75     42.8 MiB      0.3 MiB       10003           [random.randint(0, 1000) for n in range(10000)],
    76                                             ])
обьявили m_2, выделили еще 1 MiB
print(asizeof.asizeof(m_2))
# 976088

    78     43.9 MiB      1.1 MiB           1       m_3 = m_1 + m_2
обьявили m_3, выделили еще 1 MiB
print(asizeof.asizeof(m_3))
# 1189704    


memory diff: 0.7656
time diff: 0.2063
"""

import numpy as np


class Matrix_2:
    __slots__ = ['matrix']
    def __init__(self, matrix: list):
        self.matrix = np.array(matrix)

    def __iter__(self):
        return self

    def __str__(self):
        return str(self.matrix)
    #
    def __add__(self, other):
        return self.matrix + other.matrix

# @profile
@profile_time_memory
def run_2():
    m_4 = Matrix_2([
        [random.randint(0, 1000) for n in range(10000)],
        [random.randint(0, 1000) for n in range(10000)],
        [random.randint(0, 1000) for n in range(10000)],
    ])

    m_5 = Matrix_2([
        [random.randint(0, 1000) for n in range(10000)],
        [random.randint(0, 1000) for n in range(10000)],
        [random.randint(0, 1000) for n in range(10000)],
    ])

    m_6 = m_4 + m_5
    # print(asizeof.asizeof(m_4))
    # print(asizeof.asizeof(m_5))
    # print(asizeof.asizeof(m_6))


run_2()

"""
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
   139     50.5 MiB     50.5 MiB           1   @profile
   140                                         def run_2():
   141     51.6 MiB      0.1 MiB           2       m_4 = Matrix_2([
   142     50.9 MiB      0.4 MiB       10003           [random.randint(0, 1000) for n in range(10000)],
   143     51.2 MiB      0.3 MiB       10003           [random.randint(0, 1000) for n in range(10000)],
   144     51.5 MiB      0.3 MiB       10003           [random.randint(0, 1000) for n in range(10000)],
   145                                             ])
обьявили m_4, выделили 1 MiB
print(asizeof.asizeof(m_5))
# 120176

   147     51.7 MiB      0.1 MiB           2       m_5 = Matrix_2([
   148     51.6 MiB      0.0 MiB       10003           [random.randint(0, 1000) for n in range(10000)],
   149     51.6 MiB      0.0 MiB       10003           [random.randint(0, 1000) for n in range(10000)],
   150     51.6 MiB      0.0 MiB       10003           [random.randint(0, 1000) for n in range(10000)],
   151                                             ])
обьявили m_5, выделили 0.1 MiB
print(asizeof.asizeof(m_5))
# 120176

   152                                         
   153     51.7 MiB      0.0 MiB           1       m_6 = m_4 + m_5
обьявили m_6, выделили 0.1 MiB
print(asizeof.asizeof(m_6))
# 120136

memory diff: 1.14453125
time diff: 0.2047063

вывод: каждая 3х мерная матрица реализованная спомощью numpy занимает раз в 10 меньше, чем матрица из списков.
изначально выделили 1 МиБ потомучто изначально для формирования все равно нужен list comprehension, а потом вкладываем этот list в 
np.array, и так этот 1 Миб и держится для каждой очередной переменной.

можно заметить что изначально память больше на 10 МиБ по сравнению с предыдущим скриптом, но это наверное потомучто 
сама библиотека numpy навесилась сверху.

можно было б обойтись без обьявления класса, но раз уж в классах, то вот и слоты наверное чтото уменьшили, но что именно сказать трудно.

"""
