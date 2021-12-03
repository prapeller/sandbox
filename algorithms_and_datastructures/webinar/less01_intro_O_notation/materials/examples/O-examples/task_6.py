"""
Сложность: O(log n) (основанием здесь можно пренебречь)
Название: логарифмическое время

Яркий пример - двоичный (бинарный) поиск

В отсортированном наборе данных выбирается серединный элемент и
сравнивается с искомым значением.
Если значение совпадает, поиск завершен.

Если искомое значение больше, чем значение серединного элемента,
нижняя половина набора данных (все элементы с меньшими значениями,
чем у нашего серединного элемента) отбрасывается и
дальнейший поиск ведется тем же способом в верхней половине.

Если искомое значение меньше, чем значение серединного элемента,
дальнейший поиск ведется в нижней половине набора данных.

Эти шаги повторяются, при каждой итерации отбрасывая половину элементов,
пока не будет найдено искомое значение или пока оставшийся набор
данных станет невозможно разделить напополам:
"""


def binary_search(lst, number):
    start = 0
    end = len(lst) - 1

    while start <= end:
        mid = int((start + end) / 2)
        if lst[mid] == number:
            return True
        elif lst[mid] < number:
            start = mid + 1
        else:
            end = mid - 1
    return False


def find_number(lst, number):
    flag = 0
    for el in lst:
        if binary_search(el, number):
            flag += 1
    if flag == 0:
        return "Искомое число не найдено"
    else:
        return f"Искомое число встречается в {flag} коллекциях"


sorted()

number_lst = [[1, 3, 4, 2, 5, 7, 6, 8, 9], [1, 3, 4, 2, 5, 7, 6, 8, 9], [
    1, 3, 4, 2, 5, 7, 6, 8, 9], [1, 3, 4, 2, 7, 6, 8, 9]]
searched_number = 5

print(find_number(number_lst, searched_number))
