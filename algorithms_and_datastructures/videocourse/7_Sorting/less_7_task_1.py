import random

lst = [random.randint(-100, 99) for n in range(10)]


def bubble_sort(lst):
    for i in reversed(range(len(lst))):
        for j in range(i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst


print(f'random: {lst}')
print(f'sorted: {bubble_sort(lst)}')
