"""
Задание 5.**

Приведен наивный алгоритм нахождения i-го по счёту
простого числа (через перебор делителей).

Попробуйте решить эту же задачу,
применив алгоритм "Решето Эратосфена" (https://younglinux.info/algorithm/sieve)

Подсказка:
Сравните алгоритмы по времени на разных порядковых номерах чисел:
10, 100, 1000

Опишите результаты, сделайте выводы, где и какой алгоритм эффективнее
Подумайте и по возможности определите сложность каждого алгоритма.

Укажите формулу сложности О-нотация каждого алгоритма
и сделайте обоснование результатам.
"""
import cProfile


def simple(i):
    """Без использования «Решета Эратосфена»"""
    count = 1
    n = 2
    while count <= i:
        t = 1
        is_simple = True
        while t <= n:
            if n % t == 0 and t != 1 and t != n:
                is_simple = False
                break
            t += 1
        if is_simple:
            if count == i:
                break
            count += 1
        n += 1
    return n


# O((n ^ 4)/4)
def sieve(idx):
    if idx == 1:
        return 2

    # O(((len(sieve_lst))^2) / 2)
    sieve_lst = list(range(round(idx * idx / 2)))  # O(len(sieve_lst))

    for i in range(2, len(sieve_lst) - 1):  # O(len(sieve_lst))
        if sieve_lst[i] != 0:
            j = i * 2

            while j < len(sieve_lst):  # O(1/2 * len(sieve_lst))
                sieve_lst[j] = 0
                j += i

    res = [simp for simp in sieve_lst if simp != 0]  # O(len(sieve_lst))
    return res[idx]


# cProfile.run('print(simple(10))')
# cProfile.run('print(sieve(10))')
"""
29
         5 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 task_5.py:23(simple)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


29
         83 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 task_5.py:43(sieve)
        1    0.000    0.000    0.000    0.000 task_5.py:57(<listcomp>)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
       76    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.round}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""

# cProfile.run('print(simple(100))')
# cProfile.run('print(sieve(100))')
"""
541
         5 function calls in 0.002 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.002    0.002 <string>:1(<module>)
        1    0.002    0.002    0.002    0.002 task_5.py:23(simple)
        1    0.000    0.000    0.002    0.002 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


541
         11743 function calls in 0.005 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.005    0.005 <string>:1(<module>)
        1    0.003    0.003    0.005    0.005 task_5.py:43(sieve)
        1    0.000    0.000    0.000    0.000 task_5.py:57(<listcomp>)
        1    0.000    0.000    0.005    0.005 {built-in method builtins.exec}
    11736    0.001    0.000    0.001    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.round}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""

# cProfile.run('print(simple(1000))')
# cProfile.run('print(sieve(1000))')
"""
7919
         5 function calls in 0.578 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.578    0.578 <string>:1(<module>)
        1    0.578    0.578    0.578    0.578 task_5.py:23(simple)
        1    0.000    0.000    0.578    0.578 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


7919
         1400146 function calls in 0.778 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.006    0.006    0.778    0.778 <string>:1(<module>)
        1    0.575    0.575    0.772    0.772 task_5.py:44(sieve)
        1    0.022    0.022    0.022    0.022 task_5.py:59(<listcomp>)
        1    0.000    0.000    0.778    0.778 {built-in method builtins.exec}
  1400139    0.175    0.000    0.175    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.round}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""

# cProfile.run('print(simple(10000))')
# cProfile.run('print(sieve(10000))')

"""
104729
         5 function calls in 63.160 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000   63.160   63.160 <string>:1(<module>)
        1   63.160   63.160   63.160   63.160 task_5.py:23(simple)
        1    0.000    0.000   63.160   63.160 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


104729
         155549112 function calls in 92.688 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.622    0.622   92.687   92.687 <string>:1(<module>)
        1   71.689   71.689   92.058   92.058 task_5.py:43(sieve)
        1    2.030    2.030    2.030    2.030 task_5.py:57(<listcomp>)
        1    0.001    0.001   92.688   92.688 {built-in method builtins.exec}
155549105   18.340    0.000   18.340    0.000 {built-in method builtins.len}
        1    0.007    0.007    0.007    0.007 {built-in method builtins.print}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.round}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""

"""
вывод: 
в решете эратосфена есть недостаток - изначально формируется список из намного больших чисел и делается много лишних операций
я например для получения длины изначального списка (sieve_lst) сразу возвожу искомый индекс в квадрат и делю на 2 
(наверное есть и меньший множитель), но мне не удалось понять зависимость...
то есть
len(sieve_lst) = (n ^ 2) / 2
O(((len(sieve_lst))^2) / 2)
то в итоге получается 
O((n ^ 4)/4)

может, что то и напутал, но примерно в четверной степени))
судя по времени, первый алгоритм эффективней, но особо не намного. может там кубическая, сложно понять.
и этот cProfile тут особо не помогает определить потомучто всю функцию simple() он называет одним вызовом и все.

если бы была б формула зависимости простого числа от его позиции в списке натуральных чисел - то в sieve() можно было улучшить
длину изначального решета (len(sieve_lst))
а так, хз)) 

"""


def eratosfen(i):
    n = 2
    sieve_l = [n for n in range(500)]
    sieve_l[1] = 0
    for n in sieve_l:
        if sieve_l[n] != 0:
            m = n * 2
            while m < len(sieve_l):
                sieve_l[m] = 0
                m += n
    return [n for n in sieve_l if n != 0][i - 1]
