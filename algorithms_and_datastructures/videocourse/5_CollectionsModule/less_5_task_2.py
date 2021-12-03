"""
2. Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как
массив, элементы которого — цифры числа. Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и
[‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

опять же... это задание, как мне кажется, не очень удачное для демонстрации модуля collections. Только исходя из
требований задания - я использовал один раз deque(), чтоб вставку сделать в начале списка... но как понимаете можно это
было сделать и с обычным листом... может, быть, конечно у меня фантазии не хватило где можно было их использовать
"""

from collections import deque

hex_dict = {
    '0': 0,
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
    'F': 15,
}


def hex_to_dec(hex_str):
    dec = 0
    count = 1
    for n in hex_str:
        cur_dec = hex_dict[n]
        dec += cur_dec * (16 ** (len(hex_str) - count))
        count += 1

    return dec


def dec_to_hex(num: int):
    hex_list = deque()
    while num != 0:
        rem = num % 16
        for key, value in hex_dict.items():
            if value == rem:
                hex_list.appendleft(key)
        num //= 16
    return list(hex_list)


def sum_hex(hex_str_1, hex_str_2):
    dec_1 = hex_to_dec(hex_str_1)
    dec_2 = hex_to_dec(hex_str_2)
    dec_sum = dec_1 + dec_2
    return dec_to_hex(dec_sum)


def mul_hex(hex_str_1, hex_str_2):
    dec_1 = hex_to_dec(hex_str_1)
    dec_2 = hex_to_dec(hex_str_2)
    dec_mul = dec_1 * dec_2
    return dec_to_hex(dec_mul)


hex_1 = list(input('enter hex_1 (for example "A2"): '))
hex_2 = list(input('enter hex_2 (for example "C4F"): '))

print(f'hex_1 + hex_2 = {sum_hex(hex_1, hex_2)}')
print(f'hex_1 * hex_2 = {mul_hex(hex_1, hex_2)}')
