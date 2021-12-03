def my_func(x, y):
    if y < 0 and type(y) == int:
        return x ** y
    else:
        print('2nd argument should be negative integer')


print(my_func(3.25, -3))
print(my_func(3.25, -3.25))
print(my_func(3.25, 3))
print()


def my_func(x, y):
    if y < 0 and type(y) == int:
        result = 1
        for i in range(abs(y)):
            result *= (1 / x)
        return result
    else:
        print('2nd argument should be negative integer')


print(my_func(3.25, -3))
print(my_func(3.25, -3.25))
print(my_func(3.25, 3))
