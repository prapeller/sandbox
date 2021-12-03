import random

size = 10
# lst = [n for n in range(10)]
# random.shuffle(lst)
lst = [4, 0, 6, 3, 8, 2, 1, 9, 7, 5]
# lst = [5, 4, 3, 2, 1]
print(lst)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# # bubble

# for i in reversed(range(len(lst))):
#     for j in range(i):
#         if lst[j] > lst[j + 1]:
#             lst[j], lst[j + 1] = lst[j + 1], lst[j]
#
#
# print(lst)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# # selection
# # best: O(n^2), worst: O(^2)
# a)
# for i in range(len(lst)):
#     min_ind = i
#
#     for j in range(i + 1, len(lst)):
#         if lst[j] < lst[min_ind]:
#             min_ind = j
#     lst[i], lst[min_ind] = lst[min_ind], lst[i]


# b)
# for i in range(len(lst)):
#     min_ind = min(lst[i:], key=lst.__getitem__)
#     lst[i], lst[min_ind] = lst[min_ind], lst[i]
#

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# # insert
# # best: O(n), worst: O(^2)
# a)

# def insert_sort(lst):
#     for i in range(1, len(lst)):
#         for j in reversed(range(1, i + 1)):
#             if lst[j] < lst[j - 1]:
#                 lst[j], lst[j - 1] = lst[j - 1], lst[j]
#     return lst

# print(insert_sort(lst))

# b)

# def insert_sort(lst):
#     for i in range(1, len(lst)):
#         tmp = lst[i]
#         j = i
#         while lst[j-1] > tmp and j > 0:
#             lst[j] = lst[j-1]
#             j -= 1
#         lst[j] = tmp
#     return lst

# print(insert_sort(lst))

# c)
# def insert_sort(lst):
#     for i in range(1, len(lst)):
#         while i > 0 and lst[i] < lst[i - 1]:
#             lst[i], lst[i - 1] = lst[i - 1], lst[i]
#             i -= 1
#     return lst
#
# print(insert_sort(lst))

# b) shell
def shell_sort(lst):
    step = len(lst) // 2
    while step:
        for i in range(len(lst)):
            while i >= step and lst[i] < lst[i - step]:
                lst[i], lst[i - step] = lst[i - step], lst[i]
                i -= step
        step //= 2
    return lst

print(shell_sort(lst))

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# import random
#
#
# def quick_sort(lst):
#     if len(lst) < 2:
#         return lst
#     q = random.choice(lst)
#     a = [n for n in lst if n < q]
#     b = [q] * lst.count(q)
#     c = [n for n in lst if n > q]
#     return quick_sort(a) + b + quick_sort(c)
#
#
# lst = quick_sort(lst)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# charles hoarse quick sort
