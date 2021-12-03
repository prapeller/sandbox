"""Пример с алгоритмом, доступным на вашем ПК"""

import hashlib

hash_obj = hashlib.sha384(b'Testing sha384 func')
print(hash_obj)
print(hash_obj.digest())
print()

hash_obj = hashlib.sha384(b'Testing')
hash_obj.update(b' sha384 func')
print(hash_obj.digest())
print()

print(hash_obj.hexdigest())
print(hash_obj.digest())
print()

hash_obj = hashlib.new('blake2b')
print(hash_obj)
hash_obj = hashlib.blake2b()
print(hash_obj)
hash_obj.update(b'blake2b example')
print()

hash_obj = hashlib.blake2b(b'Testing sha1 func')

print(hash_obj.hexdigest())
print(hash_obj.digest())
print(hash_obj.digest_size)
print(hash_obj.block_size)