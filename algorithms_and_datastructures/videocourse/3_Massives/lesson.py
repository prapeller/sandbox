# list_1 = [1, 2, 3, 4]
# list_2 = [1, 2, 3, 4]
# list_3 = [1, 2, 3, 4]
# list_4 = [1, 2, 3, 4]
#
# for i, item in enumerate(list_1):
#

# import random


# def bin_search(array, value):
#     left = 0
#     right = len(array) - 1
#     pos = len(array) // 2
#
#     while array[pos] != value and left <= right:
#         if value > array[pos]:
#             left = pos + 1
#         else:
#             right = pos - 1
#
#         pos = (left + right) // 2
#
#     return -1 if left > right else pos
#
#
# rand_list = [random.randint(0, 1000) for _ in range(0, 100)]
# rand_list.sort()
# print(rand_list)
# n = int(input('enter integer for search: '))
# print(f'index of that integer: {bin_search(rand_list, n)}')

#
# import random
#
# less = [random.randint(-100, 100) for _ in range(100)]
# more = [less.pop(less.index(n)) for n in less if n >= 0]
#
# print(less)
# print(more)


# import random
#
# random = [random.randint(-100, 100) for _ in range(100)]
# print(random)
