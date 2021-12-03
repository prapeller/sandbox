import math


def fact(number):
    if number == 0:
        yield 1
    for n in range(1, number + 1):
        yield math.factorial(n)


for el in fact(5):
    print(el)
