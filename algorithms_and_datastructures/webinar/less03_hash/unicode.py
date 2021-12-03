# coding=utf-8

import unicodedata

# automatic utf-8
greet_rus = 'при'
print(greet_rus)

# implicit unicode
greet_rus_u = '\u043f\u0440\u0438'
print(greet_rus_u)

# to bytes (former repr())
print(greet_rus.encode())
print(greet_rus_u.encode())
print(greet_rus_u.encode('utf-8'))


# greet_eng = u'hello'
# print(greet_eng)
# print(greet_eng.encode())
# print(greet_eng.encode('utf-8'))
# print(greet_eng.encode('utf-16'))
# print(greet_eng.encode('utf-32'))
