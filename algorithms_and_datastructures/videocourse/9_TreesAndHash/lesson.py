from binarytree import tree, bst, Node, build


# class MyNode:
#
#     def __init__(self, data, left=None, right=None):
#         self.data = data
#         self.left = left
#         self.right = right
#
#
# a = tree(3, is_perfect=False)
# print(a)
#
# a = tree(3, is_perfect=True)
# print(a)
#
# b = bst(3, True)
# print(b)
#
# c = Node(7)
# c.left = Node(3)
# c.left.left = Node(1)
# c.left.right = Node(5)
# c.right = Node(11)
# c.right.left = Node(9)
# c.right.right = Node(13)
# c.left.left.left = Node(0)
# c.left.left.right = Node(2)
# c.left.right.left = Node(4)
# c.left.right.right = Node(6)
# c.right.left.left = Node(8)
# c.right.left.right = Node(10)
# c.right.right.left = Node(12)
# c.right.right.right = Node(14)
# print(c)
#
# d = build([7, 3, 11, 1, 5, 9, 13, 0, 2, 4, 6, 8, None, 12, None])
# print(d)
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
# from binarytree import bst
#
#
# def search(bin_search_tree, number, path=''):
#     if bin_search_tree.value == number:
#         return f'{number} has the following way:\nRoot{path}'
#
#     if number < bin_search_tree.value and bin_search_tree.left is not None:
#         return search(bin_search_tree.left, number, path=f'{path}\nstep left')
#
#     if number > bin_search_tree.value and bin_search_tree.right is not None:
#         return search(bin_search_tree.right, number, path=f'{path}\nstep right')
#
#     return f'theres no {number} in your tree'
#
#
# bt = bst(height=5, is_perfect=False)
# print(bt)
# num = int(input('enter search number: '))
# print(search(bt, num))

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
# h_list = [None] * 26
#
#
# def my_append(value):
#     index = ord(value[0]) - ord('a')
#     h_list[index] = value
#     print(h_list)
#
#
# a = 'apricot'
# my_append(a)
#
# b = 'banana'
# my_append(b)
#
# c = 'apple'
# my_append(c)
#
# print(4625 == 4 * 10 ** 3 + 6 * 10 ** 2 + 2 * 10 ** 1 + 5 * 10 ** 0)
#
#
# def my_index(value):
#     letter = 26
#     index = 0
#     size = 10000
#
#     for i, char in enumerate(value):
#         index += (ord(char) - ord('a') + 1) * letter ** i
#
#     return index % size
#
#
# print(my_index(a))
# print(my_index(b))
# print(my_index(c))
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
# import hashlib
#
# print(hashlib.sha1(b'Hello World!').hexdigest())
#
# s = hashlib.sha1(b'Hello World.').hexdigest()
# print(s)
#
# print(hashlib.sha1(b'sihdfaisdfs' + b'Hello World.').hexdigest())
#
# code = s.encode('utf-8')
# print(code)
#
# print(hashlib.sha1(b'sadfjng' + bytes(code)).hexdigest())
#
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # PSEVDOKID
#
# def sha1(data):
#     h0 = 0x67452301
#     h1 = 0xEFCDAB89
#     h2 = 0x98BADCFE
#     h3 = 0x10325476
#     h4 = 0xC3D2E1F0
#
#     length = len(data)
#
#     data = data << 1 + 1
#
#     if len(data) % 512 > 448:
#         data = data << 64
#
#     data = data << (448 - len(data) % 512)
#
#     data = data << 64 + length
#
#     for part_512 in data:
#         w = []
#         for i in range(16):
#             w[i] = part_512[:32]
#             part_512 = part_512[32:]
#
#         for i in range(16, 80):
#             w[i] = (w[i - 3] ^ w[i - 8] ^ w[i - 14] ^ w[i - 16]) << 1
#
#         a = h0
#         b = h1
#         c = h2
#         d = h3
#         e = h4
#
#         for i in range(80):
#             if 0 <= i <= 19:
#                 f = (b & c) | ((~b) & d)
#                 k = 0x5A827999
#
#             elif 20 <= i <= 39:
#                 f = b ^ c ^ d
#                 k = 0x6ED9EBA1
#
#             elif 40 <= i <= 59:
#                 f = (b & c) | (b & d) | (c & d)
#                 k = 0x8F1BBCDC
#
#             elif 60 <= i <= 79:
#                 f = b ^ c ^ d
#                 k = 0xCA62C1D6
#
#             temp = (a << 5) + f + e + k + w[i]
#             e = d
#             d = c
#             c = b << 30
#             b = a
#             a = temp
#
#         h0 = h0 + a
#         h1 = h1 + b
#         h2 = h2 + c
#         h3 = h3 + d
#         h4 = h4 + e
#
#     hash = h0 + h1 + h2 + h3 + h4
#
#     return hash
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# import hashlib
#
#
# def is_eq_str(a: str, b: str, verbose=False) -> bool:
#     assert len(a) > 0 and len(b) > 0, 'string cant be empty'
#
#     ha = hashlib.sha1(a.encode('utf-8')).hexdigest()
#     hb = hashlib.sha1(b.encode('utf-8')).hexdigest()
#     if verbose:
#         print(f'ha = {ha}')
#         print(f'hb = {hb}')
#
#     return ha == hb
#
#
# s_1 = input('enter string 1: ')
# s_2 = input('enter string 2: ')
#
# print('strings are equal' if is_eq_str(s_1, s_2, verbose=True) else 'string are different')

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# import hashlib
#
#
# def rabin_karp(s: str, subs: str) -> int:
#     assert len(s) > 0 and len(subs) > 0, 'string or substring cant be empty'
#     assert len(s) >= len(subs), 'substring cant be more then string'
#
#     len_sub = len(subs)
#     h_sub = hashlib.sha1(subs.encode('utf-8')).hexdigest()
#     print(f'h_sub: {h_sub}')
#
#     for i in range(len(s) - len_sub + 1):
#         h_i_sub = hashlib.sha1(s[i:i + len_sub].encode('utf-8')).hexdigest()
#         print(s[i:i+len_sub])
#         print(h_i_sub)
#         if h_sub == h_i_sub:
#             if s[i:i + len_sub] == subs:
#                 return i
#
#
# # print(hashlib.sha1('hello'.encode('utf-8')).hexdigest())
# s_1 = input('enter string: ')
# s_2 = input('enter substring for searching: ')
#
# pos = rabin_karp(s_1, s_2)
#
# print(f'substring position: {pos}' if pos is not None else 'substring not found')


