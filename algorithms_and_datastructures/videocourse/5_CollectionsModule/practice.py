a = 1

"""
в big_log.txt сервер добавляет ip. Проанализировать последние N, и сохранить в новый файл в виде "ip - количество".
исключить локальные (192.168...), сохранить исходный порядок
"""

from collections import deque, defaultdict


def write_last_n_ip(n):
    with open('big_log.txt', '+r', encoding='utf-8') as f:
        last_n_deq = deque(f, n)
        ip_qty_dict = defaultdict(int)
        for line in last_n_deq:
            if '192.168' not in line:
                ip_qty_dict[line] += 1

        with open(f'last_log_{n}.txt', 'w', encoding='utf-8') as f_1:
            for line, qty in ip_qty_dict.items():
                f_1.writelines(f'{line[:-1]}: {qty}\n')


write_last_n_ip(3000)

"""

"""
