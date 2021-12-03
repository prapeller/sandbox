"""
Задание 3.

Для этой задачи:
1) придумайте 2-3 решения (не менее двух)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.

Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.
Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.

Задание творческое. Здесь нет жестких требований к выполнению.
"""

from random import randint
import cProfile

companies = {'company_' + str(i): randint(100000, 200000) for i in range(10000)}


def get_top_3_a(comp_dict):
    """
    complexity class: O(nLogn)

    """
    sorted_comp_dict = {k: v for k, v in sorted(comp_dict.items(), key=lambda item: item[1], reverse=True)}  # O(nLogn)
    sorted_items_list = list(sorted_comp_dict.items())  # O(n)
    top_3 = []  # O(1)
    while len(top_3) < 3:  # O(1)
        top_3.append(sorted_items_list.pop(0)[0])  # 2*O(1) + O(n)
    return top_3  # O(1)


def get_top_3_b(comp_dict):
    """
    complexity class: O(n^3)
    """
    comp_dict_copy = comp_dict.copy()  # O(1)
    companies_list = list(comp_dict_copy.items())  # O(n)
    profit_list = [profit for comp, profit in comp_dict_copy.items()]  # O(n)

    top_3 = []  # O(1)

    while len(top_3) < 3:  # O(1)
        for profit in profit_list:  # O(n)
            if profit is max(profit_list):  # O(n)
                for company in companies_list:  # O(n)
                    if company[1] == profit:  # O(1)
                        top_3.append(company[0])  # O(1)
                        profit_list.remove(profit)  # O(1)

    return top_3  # O(1)


print(get_top_3_a(companies))
cProfile.run('get_top_3_a(companies)')

print(get_top_3_b(companies))
cProfile.run('get_top_3_b(companies)')

"""
вывод: функция get_top_3_a эффективней, потомучто нет вложенного цикла.
ну и плюс для выполнения условий задачи (поиск только трех компаний) лучше сначала сделать сортировку, 
иначе если больше трех компаний имеют одинаковую максимальную прибыль, то в итоговый список могут попасть все эти
компании 
"""
