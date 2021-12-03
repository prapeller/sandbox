"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы.

Сортировка должна быть реализована в виде функции.

Обязательно доработайте алгоритм (сделайте его умнее).

Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение. Обязательно сделайте замеры времени обеих реализаций
и обосновать дала ли оптимизация эффективность

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию.

Сделайте выводы!!!
Опишите в чем была ваша доработка и помогла ли вам доработка??
"""

from random import randint
from timeit import timeit


lst_worst = [n for n in range(1001)]
lst_best = [n for n in reversed(range(1001))]
lst_half = [n for n in range(501)] + [n for n in reversed(range(501))]
lst_random = [randint(-100, 100) for n in range(1001)]



def rev_bubble_sort_stupid(list_to_order):
    lst = list_to_order[:]

    for i in range(len(lst)):
        for j in reversed(range(i, len(lst) - 1)):
            if lst[j + 1] > lst[j]:
                lst[j + 1], lst[j] = lst[j], lst[j + 1]
    return lst


def rev_bubble_sort_smart(list_to_order):
    lst = list_to_order[:]
    is_sorted = False

    while not is_sorted:
        for i in range(len(lst)):
            is_sorted = True
            for j in reversed(range(i, len(lst) - 1)):
                if lst[j + 1] > lst[j]:
                    lst[j + 1], lst[j] = lst[j], lst[j + 1]
                    is_sorted = False
            if is_sorted:
                break
    return lst


ncalls = 100

print('worst case:')
print('stupid: ', timeit('rev_bubble_sort_stupid(lst_worst)', globals=globals(), number=ncalls))
print('smart: ', timeit('rev_bubble_sort_smart(lst_worst)', globals=globals(), number=ncalls))

print('best case:')
print('stupid: ', timeit('rev_bubble_sort_stupid(lst_best)', globals=globals(), number=ncalls))
print('smart: ', timeit('rev_bubble_sort_smart(lst_best)', globals=globals(), number=ncalls))

print('half case:')
print('stupid: ', timeit('rev_bubble_sort_stupid(lst_half)', globals=globals(), number=ncalls))
print('smart: ', timeit('rev_bubble_sort_smart(lst_half)', globals=globals(), number=ncalls))

print('random case:')
print('stupid: ', timeit('rev_bubble_sort_stupid(lst_random)', globals=globals(), number=ncalls))
print('smart: ', timeit('rev_bubble_sort_smart(lst_random)', globals=globals(), number=ncalls))


"""
worst case:
stupid:  13.685563499999999
smart:  14.213042699999999
в худшем для пузырька случае(когда все отсортированы в обратном порядке) - что умный, что неумный пузырек одинаков

best case:
stupid:  5.3751599999999975
smart:  0.009192499999997494
в лучшем для пузырька случае(когда все уже отсортировано как надо) - умный намного быстрей (завершается после первой же итерации)

half case:
stupid:  9.615029499999999
smart:  9.8979517
в половинном случае(когда половина упорядочена в лучшую сторону, а половина в худшую сторону) - что умный, что неумный пузырек одинаков

random case:
stupid:  11.031780400000002
smart:  11.890406199999994
в случайном случае))картина как в половинном
"""

little_bad_from_left = [n for n in range(11)] + [n for n in reversed(range(991))]
little_bad_from_right = [n for n in reversed(range(991))] + [n for n in range(11)]

print('little bad from left:')
print('stupid: ', timeit('rev_bubble_sort_stupid(little_bad_from_left)', globals=globals(), number=ncalls))
print('smart: ', timeit('rev_bubble_sort_smart(little_bad_from_left)', globals=globals(), number=ncalls))

print('little bad from right:')
print('stupid: ', timeit('rev_bubble_sort_stupid(little_bad_from_right)', globals=globals(), number=ncalls))
print('smart: ', timeit('rev_bubble_sort_smart(little_bad_from_right)', globals=globals(), number=ncalls))

"""
little bad from left:
stupid:  6.57627380000001
smart:  5.513788399999996
если небольшое количество чисел неудачно отсортировано (то есть в обратном порядке) слева  - 
то картина близка к лучшему случаю неумного пузырька как для умного, так и неумного

little bad from right:
stupid:  5.363130699999999
smart:  0.12614820000000293
но! если небольшое количество чисел неудачно отсортировано (то есть в обратном порядке) справа  - 
то умная доработка помогает.

вывод:
умная доработка с флагом помогает, но только если нужно отсортировать маленькую часть, расположенную ближе к началу 
прохода алгоритма сравнения (в нашем случае сортировка обратная, поэтому алгоритм прохода сравнения начинался справа, 
то есть пузырьки тонули), поэтому если справа у нас совсем чутка неотсорировано, а остальное (слева) отсортировано - тогда БУМ! 
рост производительности)))

а в среднем случае - что умная, что неумная - все O(n^2) 
"""
