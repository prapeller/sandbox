# import timeit
#
# x = sum(range(0, 100))
#
# print(timeit.timeit('''
# x = sum(range(0, 100))
# '''))

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# 2)

# import cProfile
#
#
# def get_len(array):
#     a = [n for n in range(100000000)]
#     return len(array)
#
#
# def get_sum(array):
#     if len(array) < 2:
#         return array[0]
#     return array[len(array) - 1] + get_sum(array[:len(array) - 1])
#
#
# def main():
#     a = [n for n in range(990)]
#     a_len = get_len(a)
#     a_len = get_len(a)
#     a_sum = get_sum(a)
#
#
# cProfile.run('main()')

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
import cProfile

# def test_fib(fib):
#     lst = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
#
#     for i, item in enumerate(lst):
#         assert item == fib(i), 'not ok'
#         print(f'{i} ok')
#
#
#
# def fib(n):
#     if n < 2:
#         return n
#     else:
#         return fib(n - 1) + fib(n - 2)
#
#
#
# test_fib(fib)
#
# # python -m timeit -n 1000 -s "import module" "module.function(param)"
#
# # "lesson_1.fib(10)"
# # 1000 loops, best of 5: 21.1 usec per loop
#
# # "lesson_1.fib(15)"
# # 1000 loops, best of 5: 255 usec per loop
#
# # "lesson_1.fib(20)"
# # 1000 loops, best of 5: 3.34 msec per loop
#
# # "lesson_1.fib(25)"
# # 1000 loops, best of 5: 33.7 msec per loop
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # ## # # # # # # # # # # # # # # # # # # # #

import functools

@functools.lru_cache()
def fib(n):
    if n < 2:
        return n
    else:
        return fib(n - 1) + fib(n - 2)

# "lesson_1.fib(10)"
# 1000 loops, best of 5: 96 nsec per loop

# "lesson_1.fib(15)"
# 1000 loops, best of 5: 91.3 nsec per loop

# "lesson_1.fib(20)"
# 1000 loops, best of 5: 96 nsec per loop

# "lesson_1.fib(25)"
# 1000 loops, best of 5: 233 nsec per loop

# "lesson_1.fib(100)"
# 1000 loops, best of 5: 239 nsec per loop

# "lesson_1.fib(200)"
# 1000 loops, best of 5: 240 nsec per loop



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# import cProfile
# cProfile.run('fib(10)')
# # 180 function calls (4 primitive calls) in 0.000 seconds
# # 177/1    0.000    0.000    0.000    0.000 lesson_1.py:44(fib)
# cProfile.run('fib(15)')
# # 1976 function calls (4 primitive calls) in 0.002 seconds
# # 1973/1    0.001    0.000    0.001    0.001 lesson_1.py:44(fib)
# cProfile.run('fib(20)')
# # 21894 function calls (4 primitive calls) in 0.013 seconds
# # 21891/1    0.012    0.000    0.012    0.012 lesson_1.py:44(fib)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# import cProfile
#
#
# def test_fib(fib):
#     lst = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
#
#     for i, item in enumerate(lst):
#         assert item == fib(i), 'not ok'
#         print(f'{i} ok')
#
#
# def fib_dict(n):
#     fib_d = {0: 0, 1: 1}
#
#     def _fib_dict(n):
#         if n in fib_d:
#             return fib_d[n]
#
#         fib_d[n] = _fib_dict(n - 1) + _fib_dict(n - 2)
#         return _fib_dict(n)
#
#     return _fib_dict(n)


# test_fib(fib_dict)

# "lesson_1.fib_dict(10)"
# 1000 loops, best of 5: 6.08 usec per loop

# "lesson_1.fib_dict(15)"
# 1000 loops, best of 5: 9.22 usec per loop

# "lesson_1.fib_dict(20)"
# 1000 loops, best of 5: 12.4 usec per loop

# "lesson_1.fib_dict(25)"
# 1000 loops, best of 5: 15.4 usec per loop

# "lesson_1.fib_dict(100)"
# 1000 loops, best of 5: 71.2 usec per loop

# "lesson_1.fib_dict(500)"
# 1000 loops, best of 5: 417 usec per loop

# cProfile.run('fib_dict(10)')
# 32 function calls (5 primitive calls) in 0.000 seconds
# 28/1    0.000    0.000    0.000    0.000 lesson_1.py:94(_fib_dict)

# cProfile.run('fib_dict(20)')
# 62 function calls (5 primitive calls) in 0.000 seconds
# 58/1    0.000    0.000    0.000    0.000 lesson_1.py:94(_fib_dict)

# cProfile.run('fib_dict(100)')
# 302 function calls (5 primitive calls) in 0.000 seconds
# 298/1    0.000    0.000    0.000    0.000 lesson_1.py:94(_fib_dict)

# cProfile.run('fib_dict(500)')
# 1502 function calls (5 primitive calls) in 0.003 seconds
# 1498/1    0.002    0.000    0.002    0.002 lesson_1.py:94(_fib_dict)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# import cProfile
#
#
# def test_fib(fib):
#     lst = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
#
#     for i, item in enumerate(lst):
#         assert item == fib(i), 'not ok'
#         print(f'{i} ok')
#
#
# def fib_loop(n):
#     if n < 2:
#         return n
#
#     first, second = 0, 1
#     for i in range(2, n + 1):
#         first, second = second, first + second
#
#     return second


# print(fib_loop(4))

# "lesson_1.fib_loop(10)"
# 1000 loops, best of 5: 792 nsec per loop
# cProfile.run('fib_loop(10)')
# 4 function calls in 0.000 seconds

# "lesson_1.fib_loop(100)"
# 1000 loops, best of 5: 6.25 usec per loop
# cProfile.run('fib_loop(100)')
# 4 function calls in 0.000 seconds

# "lesson_1.fib_loop(500)"
# 1000 loops, best of 5: 41.6 usec per loop
# cProfile.run('fib_loop(500)')
# 4 function calls in 0.000 seconds

# "lesson_1.fib_loop(50000)"
# 1000 loops, best of 5: 46.8 msec per loop
# cProfile.run('fib_loop(50000)')
# 4 function calls in 0.062 seconds
