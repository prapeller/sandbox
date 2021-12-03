def func(a, b):
    if a == b:
        return f'{a}'
    if a > b:
        return f'{a}, {func(a - 1, b)}'
    if a < b:
        return f'{a}, {func(a + 1, b)}'


print(func(1, 10))

import sys

sys.setrecursionlimit(3000)


def akk(m, n):
    if m == 0:
        return n + 1
    if m > 0 and n == 0:
        return akk(m - 1, 1)
    return akk(m - 1, akk(m, n - 1))


print(akk(3, 7))


def gcd(m, n):
    while m != n:
        if m > n:
            m -= n
        else:
            n -= m
    return m


print(gcd(24, 32))


def gcd_rec(m, n):
    if n == 0:
        return m
    return gcd_rec(n, m % n)


print(gcd_rec(24, 32))


def gcd_cycle(m, n):
    while n != 0:
        m, n = n, m % n
    return m


print(gcd_cycle(24, 32))

n = int(input('enter list maximum... '))
result = [n for n in range(n)]
result[1] = 0

for i in range(2, n):
    if result[i] != 0:
        j = i * 2
        while j < n:
            result[j] = 0
            j += i

result = [n for n in result if n != 0]
print(result)


def binary(num):
    s = ''
    while num > 0:
        s = f'{num % 2}{s}'
        num //= 2
    return s


print(binary(2))
