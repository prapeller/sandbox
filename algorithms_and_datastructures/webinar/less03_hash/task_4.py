"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносить ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования и хеш-таблиц
Можете условжнить задачу, реализовав ее через ООП
Не забудьте, что кэширование - механизм, а хеш-таблица - средство его реализации.

Задание творческое. Здесь нет жестких требований к выполнению.
"""

import hashlib

memory = dict()


def put_in_cache(url: str):
    key = hashlib.blake2b(url.encode('utf-8'), salt=url[:-3].encode('utf-8')).hexdigest()
    if key in memory:
        print(f'{url} is already in cache')
    else:
        memory[key] = url
        print(f'put "{url}" in cache')


print(memory)
put_in_cache('http://hello')
put_in_cache('http://world')
put_in_cache('http://hello')
put_in_cache('http://world')
print(memory)
