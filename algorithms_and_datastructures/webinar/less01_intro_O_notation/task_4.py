"""
Задание 4.

Для этой задачи:
1) придумайте 2-3 решения (не менее двух)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Сама задача:
Пользователи веб-ресурса проходят аутентификацию.
В системе хранятся логин, пароль и отметка об активации учетной записи.

Нужно реализовать проверку, может ли пользователь быть допущен к ресурсу.
При этом его учетка должна быть активирована.
А если нет, то польз-лю нужно предложить ее пройти.

Приложение должно давать ответы на эти вопросы и быть реализовано в виде функции.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.

Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.
Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.

Задание творческое. Здесь нет жестких требований к выполнению.
"""

import cProfile
import random

# для сравнения реализаций поиска пользователей из разных структур хранения пользователей -
# зададим максимальное кол-во пользователей для всех реализаций, чтоб потом искаль последнего (для худшего случая)
max_users_qty = 1000000


users_1 = {
    'user_' + str(i): [
        'log' + str(i),
        'pass' + str(i),
        {'is_activated': bool(random.getrandbits(1))}]
    for i in range(1, max_users_qty + 1)
}

users_2 = {
    'user_' + str(i): {
        'login': 'log' + str(i),
        'password': 'pass' + str(i),
        'is_activated': bool(random.getrandbits(1))}
    for i in range(1, max_users_qty + 1)
}

users_3 = {
    'user_id': [i for i in range(1, max_users_qty + 1)],
    'user': ['user_' + str(i) for i in range(1, max_users_qty + 1)],
    'login': ['log' + str(i) for i in range(1, max_users_qty + 1)],
    'password': ['pass' + str(i) for i in range(1, max_users_qty + 1)],
    'is_activated': [bool(random.getrandbits(1)) for i in range(1, max_users_qty + 1)]
}


def determine_user_function_1(login: str):
    """
    функция определения пользователя, вариант 1
    принимает логин
    возвращает (пользователя, пароль, флаг активации)
    класс сложности O(n)
    """
    for user, user_data in users_1.items():
        if user_data[0] == login:
            return user, user_data[1], user_data[2]


def determine_user_function_2(login: str):
    """
    функция определения пользователя, вариант 2
    принимает логин
    возвращает (пользователя, пароль, флаг активации)
    класс сложности O(n)
    """

    for user, user_data in users_2.items():
        if user_data['login'] == login:
            return user, user_data['password'], user_data['is_activated']


def determine_user_function_3(login: str):
    """
    функция определения пользователя, вариант 3
    принимает логин
    возвращает (пользователя, пароль, флаг активации)
    класс сложности O(n^2)
    """
    current_user = ''
    current_user_password = ''
    current_user_is_activated = False

    for i in range(1, len(users_3['user_id'])):
        if users_3['login'][i] == login:
            for user_id in users_3['user_id']:
                if user_id == i:
                    current_user = users_3['user'][i]
                    current_user_password = users_3['password'][i]
                    current_user_is_activated = users_3['is_activated'][i]
    return current_user, current_user_password, current_user_is_activated


users_4 = {
    'log'+str(i): ['pass' + str(i), bool(random.getrandbits(1))] for i in range(1, max_users_qty + 1)
}


def determine_user_function_4(login: str):
    """
    функция определения пользователя, вариант 3
    принимает логин
    возвращает (пользователя, пароль, флаг активации)
    класс сложности O(1)
    """
    password, is_activated = users_4[login]
    return login, password, is_activated


def run(determine_user_function):
    """
    фунция приложения
    в качестве параметра использует функцию определения пользователей
    так как класс ее сложности O(n), то она особо не влияет
    """
    determine_current_user = determine_user_function
    is_authenticated = False
    while not is_authenticated:
        try:
            login = input('enter your login: ')
            current_user, current_user_password, current_user_is_activated = determine_current_user(login)
            if current_user:
                print(f'hello, {current_user}')
                password = input('enter your password: ')

                if current_user_password == password:
                    print('password correct')
                    is_authenticated = True
                    if current_user_is_activated:
                        print('access granted')
                        break
                    else:
                        print('you should activate your account')
                        break
                else:
                    print('password incorrect')

        except TypeError:
            print('there is no such user')


if __name__ == '__main__':
    run(determine_user_function_1)
    run(determine_user_function_2)
    run(determine_user_function_3)
    run(determine_user_function_4)

# сравним выполнение алгоритмов поиска пользователей

# 1)

# cProfile.run('determine_user_function_1("log+(str(max_users_qty)")')
#          5 function calls in 0.102 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.101    0.101 <string>:1(<module>)
#         1    0.101    0.101    0.101    0.101 task_4.py:62(determine_user_function_1)
#         1    0.001    0.001    0.102    0.102 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#         1    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}

# 2)

# cProfile.run('determine_user_function_2("log+(str(max_users_qty)")')
#          5 function calls in 0.113 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.112    0.112 <string>:1(<module>)
#         1    0.112    0.112    0.112    0.112 task_4.py:74(determine_user_function_2)
#         1    0.000    0.000    0.113    0.113 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#         1    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}

# 3)

# cProfile.run('determine_user_function_3("log+(str(max_users_qty)")')
#          5 function calls in 0.082 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.082    0.082 <string>:1(<module>)
#         1    0.082    0.082    0.082    0.082 task_4.py:87(determine_user_function_3)
#         1    0.000    0.000    0.082    0.082 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# 4)
# cProfile.run("determine_user_function_4('log'+(str(max_users_qty)))")
#          4 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 task_4.py:113(determine_user_function_4)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# вывод -
# в первых двух реализациях O(n)
# в третьей O(n^2) но работает он еще быстрей!))
# сложно сказать почему так, возможно и в 3м O(n)

# в 4м реализован поиск по индексу в словаре. O(1) самый эффективный

# еще тут мне кажется имеет смысл сравнивать варианты алгоритмов формирования разных вариантов баз данных
# (users_1, users_2, users_3)
# dict comprehension работают намного медленней list comprehension
