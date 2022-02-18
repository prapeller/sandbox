"""
Задание 4.

Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
"""


def encode_decode_sandwich(str_to_endoce_decode: str) -> None:
    encoded = str_to_endoce_decode.encode('utf-8')
    print(encoded)
    decoded = encoded.decode('utf-8')
    print(decoded)


words = ['разработка', 'администрирование', 'protocol', 'standard']
for word in words:
    encode_decode_sandwich(word)
