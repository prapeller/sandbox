"""
1.	Пользователь вводит данные о количестве предприятий, их наименования и прибыль
за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.

Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections.

Пример:
Введите количество предприятий для расчета прибыли: 2
Введите название предприятия: Фирма_1
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 235 345634 55 235

Введите название предприятия: Фирма_2
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 345 34 543 34

Средняя годовая прибыль всех предприятий: 173557.5
Предприятия, с прибылью выше среднего значения: Фирма_1

Предприятия, с прибылью ниже среднего значения: Фирма_2
"""

from collections import namedtuple

companies = []
Comp = namedtuple('Comp', 'name, total')
comp_qty = 0

while True:
    try:
        comp_qty = int(input('enter companies quantity: > '))
        break
    except Exception as e:
        print(e)

while True:
    try:
        for i in range(comp_qty):
            comp_name = input(f'enter {i + 1} company name > ')
            total = sum(map(int, (input('enter company income separated by " " > ').split(sep=' '))))
            comp_nt = Comp(name=comp_name, total=total)
            companies.append(comp_nt)
        break
    except Exception as e:
        print(e, ', try again')
        companies.clear()

average_income = sum([comp.total for comp in companies]) / len(companies)

print(f'average year income per company: {average_income}')
print(f'companies above average year income: {[comp.name for comp in companies if comp.total > average_income]}')
print(f'companies below average year income: {[comp.name for comp in companies if comp.total < average_income]}')
