"""
2. Написать программу сложения и умножения двух шестнадцатиричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections
Для лучшее освоения материала можете даже сделать несколько решений этого задания,
применив несколько коллекций из модуля collections
Также попробуйте решить задачу вообще без collections и применить только ваши знания по ООП
(в частности по перегрузке методов)

__mul__
__add__

Пример:
Например, пользователь ввёл A2 и C4F.
Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’]
Произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

1. вариант
defaultdict(list)
int(, 16)
reduce

2. вариант
class HexNumber:
    __add__
    __mul__

hx = HexNumber
hx + hx
hex()
"""

from collections import deque


class HexNumber:
    hex_dict = {'0': 0,
                '1': 1,
                '2': 2,
                '3': 3,
                '4': 4,
                '5': 5,
                '6': 6,
                '7': 7,
                '8': 8,
                '9': 9,
                'A': 10,
                'B': 11,
                'C': 12,
                'D': 13,
                'E': 14,
                'F': 15, }

    @staticmethod
    def hex_to_dec(hex_str: str):
        dec = 0
        count = 1
        for n in hex_str:
            cur_dec = HexNumber.hex_dict[n.upper()]
            dec += cur_dec * (16 ** (len(hex_str) - count))
            count += 1

        return dec

    @staticmethod
    def dec_to_hex(num: int):
        hex_list = deque()
        while num != 0:
            rem = num % 16
            for key, value in HexNumber.hex_dict.items():
                if value == rem:
                    hex_list.appendleft(key)
                    break
            num //= 16
        return list(hex_list)

    def __init__(self, hex_str):
        self.dec = HexNumber.hex_to_dec(hex_str)

    def __add__(self, other):
        return HexNumber.dec_to_hex(self.dec + other.dec)

    def __mul__(self, other):
        return HexNumber.dec_to_hex(self.dec * other.dec)


hex_1 = HexNumber(input('enter hex_1 (for example "A2") > '))
print(f'hex_1 = {hex_1.dec}')
hex_2 = HexNumber(input('enter hex_2 (for example "C4F") > '))
print(f'hex_2 = {hex_2.dec}')

print(f'hex_1 + hex_2 = {hex_1 + hex_2}')
print(f'hex_1 * hex_2 = {hex_1 * hex_2}')
