import cProfile


def sieve(i):
    if i == 1:
        return 2
    sieve_lst = [n for n in range(i * i)]

    for ind in range(2, len(sieve_lst) - 1):
        if sieve_lst[ind] != 0:
            j = ind * 2

            while j < len(sieve_lst):
                sieve_lst[j] = 0
                j += ind
    res = [n for n in sieve_lst if n != 0]
    return res[i]


def prime(i):
    if i == 1:
        return 2
    res = [n for n in range(2, i * i)]

    def is_prime(n):
        d = 2
        while n % d != 0:
            d += 1
        return n == d

    prime_lst = [n for n in res if is_prime(n)]
    return prime_lst[i-1]


# print(sieve(2))
# print(prime(4))
# print(sieve(5))
# print(prime(1))

# cProfile.run('sieve(10)')
# cProfile.run('sieve(20)')
# cProfile.run('sieve(30)')
# cProfile.run('sieve(40)')
# cProfile.run('sieve(50)')

# cProfile.run('prime(10)')
# cProfile.run('prime(20)')
# cProfile.run('prime(30)')
# cProfile.run('prime(40)')
# cProfile.run('prime(50)')

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# анализ sieve()

# "less_4_task_2.sieve(10)"
# 1000 loops, best of 5: 29.3 usec per loop
# 176 function calls in 0.001 seconds

# "less_4_task_2.sieve(20)"
# 1000 loops, best of 5: 147 usec per loop
# 795 function calls in 0.001 seconds

# "less_4_task_2.sieve(30)"
# 1000 loops, best of 5: 361 usec per loop
# 1903 function calls in 0.001 seconds

# "less_4_task_2.sieve(40)"
# 1000 loops, best of 5: 790 usec per loop
# 3520 function calls in 0.002 seconds

# "less_4_task_2.sieve(50)"
# 1000 loops, best of 5: 1.17 msec per loop
# 5651 function calls in 0.002 seconds


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# анализ prime()

# "less_4_task_2.prime(10)"
# 1000 loops, best of 5: 96.3 usec per loop
# 104 function calls in 0.000 seconds

# "less_4_task_2.prime(20)"
# 1000 loops, best of 5: 1.23 msec per loop
# 404 function calls in 0.002 seconds

# "less_4_task_2.prime(30)"
# 1000 loops, best of 5: 5.54 msec per loop
# 904 function calls in 0.012 seconds

# "less_4_task_2.prime(40)"
# 1000 loops, best of 5: 17.4 msec per loop
# 1604 function calls in 0.032 seconds


# "less_4_task_2.prime(50)"
# 1000 loops, best of 5: 39.8 msec per loop
# 2504 function calls in 0.038 seconds


# вывод: sieve быстрей, так как prime задействует дополнительную проверку, которая нагружает алгоритм еще на
# порядок вычислений..

