import copy
import random

from memory_profiler import memory_usage
from memory_profiler import profile
from timeit import default_timer
from collections import Counter


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
функция из задания 4 урока 4.
"""

# @profile
@profile_time_memory
def get_most_frequent():
    array = [random.randint for n in range(100000)]
    local_arr = copy.deepcopy(array)
    counter = Counter(local_arr)
    elem_4, max_4 = counter.most_common(1)[0]
    return f'Чаще всего встречается число {elem_4}, ' \
           f'оно появилось в массиве {max_4} раз(а)'


# get_most_frequent()

"""
рез-ты работы @profile:

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    29     40.7 MiB     40.7 MiB           1   @profile
    30                                         def get_most_frequent():
    31     42.2 MiB      1.4 MiB      100003       array = [random.randint for n in range(100000)]
добавился array
    32     43.0 MiB      0.8 MiB           1       local_arr = copy.deepcopy(array)
добавился local_array
    33     43.0 MiB      0.0 MiB           1       counter = Counter(local_arr)
    34     43.0 MiB      0.0 MiB           1       elem_4, max_4 = counter.most_common(1)[0]
    35     43.0 MiB      0.0 MiB           2       return f'Чаще всего встречается число {elem_4}, ' \
    36     43.0 MiB      0.0 MiB           1              f'оно появилось в массиве {max_4} раз(а)'
увеличение на 2.3 МiB

рез-ты работы @profile_time_memory
memory diff: 0.33984375
time diff: 0.1569

"""

# @profile
@profile_time_memory
def get_most_frequent_2():
    array = [random.randint for n in range(100000)]
    local_arr = copy.deepcopy(array)
    del array
    counter = Counter(local_arr)
    elem_4, max_4 = counter.most_common(1)[0]
    del local_arr
    return f'Чаще всего встречается число {elem_4}, ' \
           f'оно появилось в массиве {max_4} раз(а)'


get_most_frequent_2()

"""
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    65     40.5 MiB     40.5 MiB           1   @profile
    66                                         def get_most_frequent_2():
    67     42.0 MiB  -3819.4 MiB      100003       array = [random.randint for n in range(100000)]
добавился array, по mem usage видно что расходование памяти увеличилсь гдето на 1.5 MiB

    68     42.8 MiB      0.8 MiB           1       local_arr = copy.deepcopy(array)
добавился local_array, расходование памяти увеличилсь 0.8 MiB

    69     41.3 MiB     -1.5 MiB           1       del array
удалился array, расходование памяти уменьшилось 1.5 MiB

    70     41.3 MiB      0.0 MiB           1       counter = Counter(local_arr)
    71     41.3 MiB      0.0 MiB           1       elem_4, max_4 = counter.most_common(1)[0]
    72     40.5 MiB     -0.8 MiB           1       del local_arr
удалился local_array, расходование памяти уменьшилось 0.8 MiB

    73     40.5 MiB      0.0 MiB           2       return f'Чаще всего встречается число {elem_4}, ' \
    74     40.5 MiB      0.0 MiB           1              f'оно появилось в массиве {max_4} раз(а)'
с чего начали к тому и пришли (40.5 MiB)

рез-ты работы @profile_time_memory
memory diff: 0.11328125
time diff: 0.1773
по самописному мало что понятно о работе памяти во время выполнения функции.
"""
