"""
Служебный скрипт запуска/останова нескольких клиентских приложений
"""

from subprocess import Popen


P_LIST = []

while True:
    USER = input("Запустить 10 клиентов (s) / Закрыть клиентов (x) / Выйти (q) ")

    if USER == 'q':
        break

    elif USER == 's':
        for _ in range(10):

            P_LIST.append(Popen(['python', 'time_client_random.py'], shell=True))

        print(' Запущено 10 клиентов')
    elif USER == 'x':
        for p in P_LIST:
            p.kill()
        P_LIST.clear()
