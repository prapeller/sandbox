import time

# 1
my_list_1 = [2, 2, 2, 2, 5, 5, 8, 2, 12, 12, 4]
my_list_2 = [2, 7, 12, 3]

# a) iterating list elements
for number in my_list_1[:]:
    if number in my_list_2:
        my_list_1.remove(number)
print(my_list_1)

# b) list comprehensions
list_1_without_list_2_b = [number for number in my_list_1 if number not in my_list_2]
print(list_1_without_list_2_b)

# 2
days_list = [
    'первое',
    'второе',
    'третье',
    'четвертое',
    'пятое',
    'шестое',
    'седьмое',
    'восьмое',
    'девятое',
    'десятое',
    'одиннадцатое',
    'двенадцатое',
    'тринадцатое',
    'четырнадцатое',
    'пятнадцатое',
    'шестнадцатое',
    'семнадцатое',
    'восемьнадцатое',
    'девятнадцатое',
    'двадцатое',
    'двадцать первое',
    'двадцать второе',
    'двадцать третье',
    'двадцать четвертое',
    'двадцать пятое',
    'двадцать шестое',
    'двадцать седьмое',
    'двадцать восьмое',
    'двадцать девятое',
    'тридцатое',
    'тридцать первое'
]

month_list = [
    'января',
    'февраля',
    'марта',
    'апреля',
    'мая',
    'июня',
    'июля',
    'августа',
    'сентября',
    'октября',
    'ноября',
    'декабря'
]
string_date = '02.11.2013'
time_tuple = time.strptime(string_date, '%d.%m.%Y')
day_number = time_tuple.tm_mday
month_number = time_tuple.tm_mon
year_number = time_tuple.tm_year
result_string = f'{days_list[day_number - 1]} {month_list[month_number - 1]} {year_number} года.'
print(result_string)

# 3
my_list_3 = [1, 1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 9, 10, 10]

# a) iterating list elements
my_list_4 = []
for number in my_list_3:
    if my_list_3.count(number) == 1:
        my_list_4.append(number)
print(my_list_4)

# b) list comprehensions
my_list_5 = [number for number in my_list_3 if my_list_3.count(number) == 1]
print(my_list_5)
