# print(id(100))
# a = 120 - 20
# print(id(a))
# print(id(1000))
# b = 1020 - 20
# print(id(b))

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# a = 42
# print(a)
# print(a >> 1)
# print(bin(a))
# print(oct(a))
# print(hex(a))
#
# allocated = 0
# for newsize in range(100):
#     if allocated < newsize:
#         new_allocated = (newsize >> 3) + (3 if newsize < 9 else 6)
#         allocated = newsize + new_allocated
#
#     print(newsize, allocated)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

import sys

print(sys.version, sys.platform, sep='\n')
a = 5
b = 123.12
c_0 = ''
c = 'string'
d = 'string'*2
e = [n for n in range(100)]
f = tuple(e)
g = set(e)
h = {str(n): n for n in range(100)}


def show_size(x, level=0):
    print('\t' * level, f'type={x.__class__},\t size={sys.getsizeof(x)},\t object={x}')

    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for xx in x.items():
                show_size(xx, level + 1)
        elif not isinstance(x, str):
            for xx in x:
                show_size(xx, level + 1)
#
#
# show_size(a)
# show_size(b)
# show_size(c_0)
# show_size(c)
# show_size(d)
# show_size(e)
# show_size(f)
# show_size(g)
# show_size(h)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# import sys
# import ctypes
# import struct
#
#
# a = 3
# x = y = a
# b = 123.12
# c = 'string'
# e = [n for n in range(10)]
# f = tuple(e)
# g = set(e)
# h = {str(n): n for n in range(10)}
#
# show_size(None)
# show_size(3)
# print(id(a))
# print(sys.getsizeof(a))
# print(f'ctypes.string_at(id()): {ctypes.string_at(id(5))}')
# print(f'ctypes.string_at(id(), size=...): {ctypes.string_at(id(5), size=sys.getsizeof(5))}')
# print(struct.unpack('LLLLLLl', ctypes.string_at(id(a), sys.getsizeof(a))))
# print(id(int))
