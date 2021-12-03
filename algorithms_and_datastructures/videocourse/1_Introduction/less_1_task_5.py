# 5. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

# draw.io diagram:
# https://drive.google.com/file/d/18PboRrtDEjb_oNSClRS7cIQBwI37RGH-/view?usp=sharing

x = int(input('enter any number from 1 to 32... '))
if x in range(27):
    print(f"{x}'th character in english alphabet - {chr(x + 96)}, in russian alphabet - {chr(x + 1071)}")
elif x in range(27, 33):
    print(f"{x}'th character in russian alphabet - {chr(x + 1071)}")
else:
    print('there are no such characters in russian or english abc')

