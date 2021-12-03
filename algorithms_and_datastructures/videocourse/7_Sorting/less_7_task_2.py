import random

lst = [round(random.uniform(0, 49), 2) for n in range(10)]


def merge_sort(lst):
    count = len(lst)
    if count > 2:
        part_1 = merge_sort(lst[:count // 2])
        part_2 = merge_sort(lst[count // 2:])
        lst = part_1 + part_2
        last_index = len(lst) - 1

        for i in range(last_index):
            min_value = lst[i]
            min_index = i

            for j in range(i + 1, last_index + 1):
                if min_value > lst[j]:
                    min_value = lst[j]
                    min_index = j

            if min_index != i:
                lst[i], lst[min_index] = lst[min_index], lst[i]

    elif len(lst) > 1 and lst[0] > lst[1]:
        lst[0], lst[1] = lst[1], lst[0]

    return lst


def bose_nelson(lst):
    def bose_nelson_merge(j, r, m):
        if j + r < len(lst):
            if m == 1:
                if lst[j] > lst[j + r]:
                    lst[j], lst[j + r] = lst[j + r], lst[j]
            else:
                m = m // 2
                bose_nelson_merge(j, r, m)
                if j + r + m < len(lst):
                    bose_nelson_merge(j + m, r, m)
                bose_nelson_merge(j + m, r - m, m)
        return lst

    m = 1
    while m < len(lst):
        j = 0
        while j + m < len(lst):
            bose_nelson_merge(j, m, m)
            j = j + m + m
        m = m + m

    return lst


print(lst)
print(merge_sort(lst[:]))
print(bose_nelson(lst[:]))
