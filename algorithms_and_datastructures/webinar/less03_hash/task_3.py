"""
Задание 3.
Определить количество различных (уникальных) подстрок с использованием хеш-функции.
Дана строка S длиной N, состоящая только из строчных латинских букв.

Подсказка: примените вычисление хешей для подстрок с помощью хеш-функций и множества
Можно воспользоваться ф-цией hash() (см. материалы к уроку)

Пример:
рара - 6 уникальных подстрок

рар
ра
ар
ара
р
а
"""

import hashlib


def get_substr_set(string: str) -> set:
    substr_set = set()
    substr_hash_set = set()

    for i in range(1, len(string)):
        sub_i = string[:-i]
        sub_i_hash = hashlib.sha256(sub_i.encode('utf-8')).hexdigest()

        substr_set.add(sub_i)
        substr_hash_set.add(sub_i_hash)

        for n in range(i + 1):
            sub_i_shifted = string[n:n + len(sub_i)]
            sub_i_shifted_hash = hashlib.sha256(sub_i_shifted.encode('utf-8')).hexdigest()

            if sub_i_shifted_hash not in substr_hash_set:
                substr_set.add(sub_i_shifted)
                substr_hash_set.add(sub_i_shifted_hash)

    return substr_set


if __name__ == '__main__':
    user_str = input('enter string: ')
    user_substr_set = get_substr_set(user_str)
    print(f'quantity of substring in "{user_str}": {len(user_substr_set)}')

    for substr in user_substr_set:
        print(substr)
