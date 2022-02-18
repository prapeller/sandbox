"""
Задание 2.

Каждое из слов «class», «function», «method» записать в байтовом формате
без преобразования в последовательность кодов
не используя!!! методы encode и decode)
и определить тип, содержимое и длину соответствующих переменных.

Подсказки:
--- b'class' - используйте маркировку b''
--- используйте списки и циклы, не дублируйте функции
"""

strings_list = ['class', 'function', 'method']
for string in strings_list:
    print(string, type(string))

bytes_seq_list = [b'class', b'function', b'method']
for bytes_seq in bytes_seq_list:
    print(bytes_seq, type(bytes_seq), len(bytes_seq))
