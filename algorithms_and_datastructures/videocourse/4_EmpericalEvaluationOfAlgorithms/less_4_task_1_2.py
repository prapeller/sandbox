import cProfile
import sys
sys.setrecursionlimit(2000)

# Из lesson 2 task 2.Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число
# 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

# Будем анализировать временную сложность алгоритма в зависимости от длины входного числа n.
# Чем больше index, тем длиннее будет число из последовательности 0, 1, 12, 123, 1234 ... n(i-1) * 10 + i

# i, 0, 1, 12, ... (i-1) * 10 + i

# 0, 0
# 1, 1
# 2, 12
# 3, 123
# 4, 1234
# 5, 12345

# учитывая что функция input возвращает строку, то для начала сделаем неизменяемый во всех реализациях рекурсивный
# алгоритм формирования строчного представления натурального числа n,


def make_integer_str(length):
    def make_integer(i):
        if i == 0:
            return 0
        return make_integer(i - 1) * 10 + i

    return str(make_integer(length))


# а далее будем пытаться оптимизировать алгоритм подсчета количества четных и нечетных цифр в этом числе...

# реализация 1)
def count_even_odd_1(integer):
    n = 0
    count_even = 0
    count_odd = 0

    integer = int(integer)
    while integer > 0:
        n = integer % 10
        integer //= 10
        if n % 2 == 0:
            count_even += 1
        else:
            count_odd += 1
    # print(f'even numbers: {count_even}')
    # print(f'odd numbers: {count_odd}')
    return count_even, count_odd


# реализация 2)
def count_even_odd_2(integer):
    num_str = integer
    count_even = 0
    count_odd = 0
    for num in num_str:
        if int(num) % 2 == 0:
            count_even += 1
        else:
            count_odd += 1
    # print(f'even numbers: {count_even}')
    # print(f'odd numbers: {count_odd}')
    return count_even, count_odd


# выход у реализаций одинаковый, можете раскомментить внутри них print(), чтоб убедиться


# count_even_odd_1(make_integer_str(3))
# count_even_odd_2(make_integer_str(3))

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# замерим время на алгоритм формирования числа длиной 10, 20, 50, 100, 200, 500 и 900, 1900 цифр-
# чтоб можно было это время не учитывать при замерах алгоритма подсчета четных и нечетных цифр.
#  для числа длиной 1900 увеличим стек рекурсии...

# "less_4_task_1_2.make_integer_str(10)"
# 1000 loops, best of 5: 2.36 usec per loop

# "less_4_task_1_2.make_integer_str(20)"
# 1000 loops, best of 5: 4.7 usec per loop

# "less_4_task_1_2.make_integer_str(50)"
# 1000 loops, best of 5: 12.1 usec per loop

# "less_4_task_1_2.make_integer_str(200)"
# 1000 loops, best of 5: 56.7 usec per loop

# "less_4_task_1_2.make_integer_str(500)"
# 1000 loops, best of 5: 256 usec per loop

# "less_4_task_1_2.make_integer_str(900)"
# 1000 loops, best of 5: 434 usec per loop

# "less_4_task_1_2.make_integer_str(1900)"
# 1000 loops, best of 5: 1.6 msec per loop

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# "less_4_task_1_2.count_even_odd_1(less_4_task_1_2.make_integer_str(10))"
# 1000 loops, best of 5: 4.43 usec per loop-2.36=
# 2.07
# 16 function calls (6 primitive calls) in 0.001 seconds

# "less_4_task_1_2.count_even_odd_1(less_4_task_1_2.make_integer_str(20))"
# 1000 loops, best of 5: 8.95 usec per loop-4,7=
# 4.25
# 26 function calls (6 primitive calls) in 0.001 seconds

# "less_4_task_1_2.count_even_odd_1(less_4_task_1_2.make_integer_str(50))"
# 1000 loops, best of 5: 23.1 usec per loop-12.1=
# 11
# 56 function calls (6 primitive calls) in 0.000 seconds

# "less_4_task_1_2.count_even_odd_1(less_4_task_1_2.make_integer_str(200))"
# 1000 loops, best of 5: 151 usec per loop - 56.7=
# 94.3
# 206 function calls (6 primitive calls) in 0.001 seconds

# "less_4_task_1_2.count_even_odd_1(less_4_task_1_2.make_integer_str(500))"
# 1000 loops, best of 5: 449 usec per loop -256=
# 193
# 506 function calls (6 primitive calls) in 0.002 seconds

# "less_4_task_1_2.count_even_odd_1(less_4_task_1_2.make_integer_str(900))"
# 1000 loops, best of 5: 1.1 msec per loop-0.434=
# 666
# 906 function calls (6 primitive calls) in 0.003 seconds

# "less_4_task_1_2.count_even_odd_1(less_4_task_1_2.make_integer_str(1900))"
# 1000 loops, best of 5: 4.31 msec per loop-1.6=
# 2,71

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# "less_4_task_1_2.count_even_odd_2(less_4_task_1_2.make_integer_str(10))"
# 1000 loops, best of 5: 4.77 usec per loop-2.36=
# 2,41
# 16 function calls (6 primitive calls) in 0.001 seconds

# "less_4_task_1_2.count_even_odd_2(less_4_task_1_2.make_integer_str(20))"
# 1000 loops, best of 5: 9.21 usec per loop-4.7=
# 4.51
# 26 function calls (6 primitive calls) in 0.000 seconds

# "less_4_task_1_2.count_even_odd_2(less_4_task_1_2.make_integer_str(50))"
# 1000 loops, best of 5: 23.4 usec per loop-12.1=
# 12
# 56 function calls (6 primitive calls) in 0.000 seconds

# "less_4_task_1_2.count_even_odd_2(less_4_task_1_2.make_integer_str(200))"
# 1000 loops, best of 5: 112 usec per loop - 56.7=
# 55
# 206 function calls (6 primitive calls) in 0.000 seconds

# "less_4_task_1_2.count_even_odd_2(less_4_task_1_2.make_integer_str(500))"
# 1000 loops, best of 5: 302 usec per loop -256=
# 46
# 506 function calls (6 primitive calls) in 0.001 seconds

# "less_4_task_1_2.count_even_odd_2(less_4_task_1_2.make_integer_str(900))"
# 1000 loops, best of 5: 645 usec per loop-434=
# 211
# 906 function calls (6 primitive calls) in 0.003 seconds

# "less_4_task_1_2.count_even_odd_2(less_4_task_1_2.make_integer_str(1900))"
# 1000 loops, best of 5: 1.96 msec per loop-1.6=
# 360

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# выводы... при длине числа свыше 500 цифр - первый алгоритм растет быстрее нежели второй.
# следовательно для решения этой зачачи имеет смысл перебирать символы, а не вычислять остаток от деления на 10...







