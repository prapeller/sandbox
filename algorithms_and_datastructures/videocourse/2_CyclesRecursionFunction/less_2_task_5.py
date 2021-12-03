# 5. Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
# Вывод выполнить в табличной форме: по десять пар «код-символ» в каждой строке.

# draw.io diagram:
# https://drive.google.com/file/d/1u7wgsKpvxdWEgdnMBed7JaswGAvL1a59/view?usp=sharing

import itertools

counter = itertools.count(32)
line_count = 0

for i in range(32, 128):
    current_code = counter.__next__()
    str = f'{current_code}-"{chr(i)}"\t'
    print(str, end='')
    line_count += 1
    if line_count % 10 == 0:
        print()