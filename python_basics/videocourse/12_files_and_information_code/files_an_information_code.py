# file = open('first.txt', 'w')
# file = open('first.txt', 'a')
# file.write('hello world\n')
# file.write('hi again\n')
# file.writelines(['this is additional line\n', 'and this is one more else'])
#
#
# file = open('first.txt', 'r')
# print(file.read())
# file.close()
#
# file = open('first.txt', 'r')
# for s in file:
#     print(s.replace('\n', ''))
# file.close()
#
# file = open('first.txt', 'r')
# print(file.readlines())
# file.close()
#
#
# with open('first.txt', 'r') as file:
#     print(file.read())
#
# with open('first.txt', 'r') as file:
#     for s in file:
#         print(s.replace('\n', ''))
#
# with open('first.txt', 'r') as file:
#     print(file.readlines())
#
# s = 'hello world'
# print(s)
# print(type(s))
# print(s[1])
# print(s[1:3])
#
# sb = b'hello world'
# print(sb)
# print(type(sb))
# print(sb[1])
# print(sb[1:3])
# for byte in sb:
#     print(byte)
#
# utf_text = 'hello мир 你好 再见'
# bytes_utf_text = utf_text.encode('utf-8')
# print(bytes_utf_text)
# utf_text = bytes_utf_text.decode('utf-8')
# print(utf_text)
#
# print(s.encode('ascii'))
#
#
# with open('bytes_text', 'wb') as bytes_file:
#     bytes_file.write(b'hello')
#
# with open('bytes_text', 'rb') as bytes_file:
#     print(bytes_file.read())
#
#
# with open('bytes_utf_text', 'wb') as bytes_file:
#     bytes_to_write = 'мир 你好'.encode('utf-8')
#     bytes_file.write(bytes_to_write)
#
# with open('bytes_utf_text', 'rb') as bytes_file:
#     bytes_to_read = bytes_file.read()
#     print(bytes_to_read, type(bytes_to_read))
#     string = bytes_to_read.decode('utf-8')
#     print(string, type(string))
#
# with open('bytes_utf_text', 'w', encoding='utf-8') as file:
#     file.write('мир 你好')
#
# with open('bytes_utf_text', 'r', encoding='utf-8') as file:
#     print(file.read())


person = {'name: ': 'Pablo', 'gender': 'male', 'age: ': '34', 'phones: ': [89857655302, 89250470366]}

# with open('person.dat', 'wb') as f:
#     for key, value in person.items():
#         print(key, value)
#         if key == 'phones: ':
#             f.write(key.encode('utf-8'))
#             for phone in value:
#                 f.write((str(phone)+', ').encode('utf-8'))
#         else:
#             f.write(key.encode('utf-8'))
#             f.write((value+', ').encode('utf-8'))

import pickle

# with open('person.dat', 'wb') as f:
#     pickle.dump(person, f)
#
with open('person.dat', 'rb') as f:
    loaded_person = pickle.load(f)

print(loaded_person)

import json

# # to memory
# json_person = json.dumps(person)
# print(json_person, type(json_person))

# loaded_person = json.loads(json_person)
# print(loaded_person, type(loaded_person))

# # to file
# with open('person.json', 'w') as f:
#     json.dump(person, f)
#
# with open('person.json', 'r') as f:
#     loaded_from_file_json_person = json.load(f)
#
# print(loaded_from_file_json_person, type(loaded_from_file_json_person))



