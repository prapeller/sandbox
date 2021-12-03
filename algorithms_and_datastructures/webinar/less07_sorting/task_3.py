"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные по длине части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы.

Задачу можно решить без сортировки исходного массива.

Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках: Шелла, Гномья, Кучей...

[5, 3, 4, 3, 3, 3, 3]

[3, 3, 3, 3, 3, 4, 5]

my_lst
new_lts

arr[m]


from statistics import median

[3, 4, 3, 3, 5, 3, 3]

left = []
right = []

left == right and

for i in
    for
    left == right
    left.clear()
    right.clear()


"""

from statistics import median
import random

# m = int(input('enter "m" > '))
# arr = [random.randint(0, 10) for _ in range(2 * m + 1)]
# print(arr)
arr = [2, 8, 0, 3, 7]
print()


print(f'statistics median: \t{median(arr)}')


def quick_median(lst, k):
    pivot = random.choice(lst)

    lowers = [n for n in lst if n < pivot]
    pivots = [n for n in lst if n == pivot]
    highers = [n for n in lst if n > pivot]

    if len(lowers) > k:
        return quick_median(lowers, k)
    elif len(lowers + pivots) > k:
        return pivot
    else:
        return quick_median(highers, k - len(lowers + pivots))


print(f'quick:  \t\t\t{quick_median(arr, len(arr) // 2)}')


def iterable_median(lst):
    for i in range(len(lst)):
        lowers = []
        highers = []
        pivots = []
        for j in range(len(lst)):
            if lst[j] < lst[i] and i != j:
                lowers.append(lst[j])
            if lst[j] > lst[i] and i != j:
                highers.append(lst[j])
            if lst[j] == lst[i] and i != j:
                pivots.append(lst[j])

        for k in range(len(pivots) + 1):
            if len(highers) - k == len(lowers):
                return lst[i]
            if len(lowers) - k == len(highers):
                return lst[i]


print(f'iterable 1: \t\t{iterable_median(arr[:])}')


def iterable_median_2(lst):
    for i in range(len(lst)):
        lowers = []
        highers = []
        for j in range(len(lst)):
            if lst[i] > lst[j] or lst[i] == lst[j] and i > j:
                lowers.append(lst[j])
            if lst[i] < lst[j] or lst[i] == lst[j] and i < j:
                highers.append(lst[j])
        if len(lowers) == len(highers):
            return lst[i]


print(f'iterable 2:  \t\t{iterable_median_2(arr[:])}')


def median_with_shell_sort(lst):
    step = len(lst) // 2
    while step:
        for i in range(len(lst)):
            while i >= step and lst[i] < lst[i - step]:
                lst[i], lst[i - step] = lst[i - step], lst[i]
                i -= step
        step //= 2
    return lst[len(lst) // 2]


print(f'shell:  \t\t\t{median_with_shell_sort(arr[:])}')


def median_with_gnome_sort(lst):
    i = 1
    while i < len(lst):
        if i == 0 or lst[i - 1] <= lst[i]:
            i += 1
        else:
            lst[i], lst[i - 1] = lst[i - 1], lst[i]
            i -= 1
    return lst[len(lst) // 2]


print(f'gnome: \t\t\t\t{median_with_gnome_sort(arr[:])}')

