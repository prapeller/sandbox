import random

rand_lst = [random.randint(10, 100) for n in range(11)]
print(rand_lst)


def find_median(lst):
    for i in range(len(lst) - 1):
        for j in range(i, len(lst)):
            if lst[j] < lst[i]:
                lst[i], lst[j] = lst[j], lst[i]
    return lst[len(lst) // 2]


med = find_median(rand_lst[:])
print(f'\nmedian >>>>>>>>>>>>> {med}')
print(sorted(rand_lst[:]))


# def heap_bottom_up(data):
#     for start in range((len(data) - 2) // 2, -1, -1):
#         heap_bottom_up_shift(data, start, len(data) - 1)
#     for end in range(len(data) - 1, 0, -1):
#         data[end], data[0] = data[0], data[end]
#         heap_bottom_up_shift(data, 0, end - 1)
#     return data
#
#
# def heap_bottom_up_leaf_search(data, start, end):
#     current = start
#     while True:
#         child = current * 2 + 1
#         if child + 1 > end:
#             break
#         if data[child + 1] > data[child]:
#             current = child + 1
#         else:
#             current = child
#
#     child = current * 2 + 1
#     if child <= end:
#         current = child
#
#     return current
#
#
# def heap_bottom_up_shift(data, start, end):
#     current = heap_bottom_up_leaf_search(data, start, end)
#
#     while data[start] > data[current]:
#         current = (current - 1) // 2
#
#     temp = data[current]
#     data[current] = data[start]
#
#     while current > start:
#         current = (current - 1) // 2
#         temp, data[current] = data[current], temp
#
#
# print(heap_bottom_up(rand_lst[:]))
