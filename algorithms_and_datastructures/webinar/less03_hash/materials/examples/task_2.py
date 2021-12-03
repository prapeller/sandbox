"""Примеры с md5"""

import hashlib
# функции хеширования hashlib.md5 / hashlib.sha1
# принимают строку-байт, поэтому если текст не латиница - для перевода в байты нужно кодировать через utf-8

print('testing'.encode('utf-8'))
# b'testing' ------ ok
print('тестинг'.encode('utf-8'))
# b'\xd1\x82\xd0\xb5\xd1\x81\xd1\x82\xd0\xb8\xd0\xbd\xd0\xb3'  -------- ok


hash_obj = hashlib.md5(b'Testing')

print(hash_obj)
# <md5 HASH object @ 0x0000021C4B589A20>
print(type(hash_obj))
# <class '_hashlib.HASH'>
print()


hash_hex_str = hash_obj.hexdigest()
print(hash_hex_str)
# fa6a5a3224d7da66d9e0bdec25f62cf0
print(type(hash_hex_str))
# <class 'str'>
print()

hash_obj_2 = hashlib.sha1(("Тестинг").encode('utf-8'))
print(hash_obj_2)
# <md5 HASH object @ 0x0000021C4D53ED50>

print(type(hash_obj_2))
# <class '_hashlib.HASH'>
hash_hex_str_2 = hash_obj_2.hexdigest()
print(hash_hex_str_2)
print(type(hash_hex_str_2))

# python -> json-строка -> байты
