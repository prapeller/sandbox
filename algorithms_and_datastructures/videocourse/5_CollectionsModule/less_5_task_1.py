"""
1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за четыре квартала для каждого
предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести наименования
предприятий, чья прибыль выше среднего и ниже среднего.

Для тестирования скопируйте строчки ниже, например. 4 конторы, доход "company_1" = 200, "company_2" = 300 и тд.
Вообще, это задание, как мне кажется, не очень удачное для демонстрации модуля collections. Только исходя из
требований задания - я использовал OrderedDict(), но если вы вместо этого поставите regular dict (companies = {})
или поставите defaultdict (companies = defaultdict(float)) - все по прежнему будет работать.

4
200
company_1
300
company_2
400
company_3
500
company_4

"""
from collections import OrderedDict


n = int(input('enter companies quantity: '))
companies = OrderedDict()

for _ in range(n):
    companies[input('enter company name: ')] = float(input('enter company income: '))

average_income = round(sum(companies.values()) / len(companies), 2)
print(f'average income: {average_income}')

upper_average = [name for name, income in companies.items() if income > average_income]
print(f'upper then average: {upper_average}')

lower_average = [name for name, income in companies.items() if income < average_income]
print(f'lower then average: {lower_average}')
