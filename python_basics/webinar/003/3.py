def my_func(a, b, c):
    abc_tuple = a, b, c
    abc_list = list(abc_tuple)
    abc_list.remove(min(abc_tuple))
    return sum(abc_list)


print(my_func(1.25, 2.25, 3))
