"""
Задание 2.
Ваша программа должна запрашивать пароль
Для этого пароля вам нужно получить хеш, используя функцию sha256
Для генерации хеша обязательно нужно использовать криптографическую соль
Обязательно выведите созданный хеш.

Далее программа должна запросить пароль повторно
Вам нужно проверить, совпадает ли пароль с исходным
Для проверки необходимо сравнить хеши паролей

ПРИМЕР:
Введите пароль: 123
В базе данных хранится строка: 555a3581d37993843efd4eba1921f1dcaeeafeb855965535d77c55782349444b
Введите пароль еще раз для проверки: 123
Вы ввели правильный пароль

Обязательно усложните задачу! Добавьте сохранение хеша в файле и получение его из файла.
А если вы знаете как через Python работать с БД, привяжите к заданию БД и сохраняйте хеши там.
"""

import sqlite3
import hashlib


def register_without_sql_injection_possibility(login, password):
    insert_query = "insert into users values (?, ?);"
    new_hash = hashlib.sha256(login.encode('utf-8') + password.encode('utf-8')).hexdigest()
    new_user = login, new_hash
    cursor.execute(insert_query, new_user)
    conn.commit()


# registering loop
def register():
    print('REGISTER MODE STARTED')
    while True:
        user_choice = input('want to register? [y/n] > ')
        if user_choice == 'n':
            print('REGISTER MODE FINISHED\n')
            break
        user_login = input('enter your login to register > ')
        user_password = input('enter your password to register > ')
        try:
            register_without_sql_injection_possibility(login=user_login, password=user_password)
        except sqlite3.IntegrityError as e:
            print('this login already used.', e)


def check_password(login, password):
    select_pass_query = "select password_hash from users where login = (?)"
    db_password_hash = cursor.execute(select_pass_query, (login,)).fetchone()[0]

    hash_from_passed_password = hashlib.sha256(login.encode('utf-8') + password.encode('utf-8')).hexdigest()

    if db_password_hash == hash_from_passed_password:
        return True, db_password_hash
    else:
        return False, None


def login():
    print('LOGIN MODE STARTED')
    while True:
        user_login = input('enter your login > ')
        user_password = input('enter you password > ')
        is_logged_in, user_password_hash = check_password(user_login, user_password)
        if is_logged_in:
            print(f'your password hash: {user_password_hash}')
            print('you are logged in')
            print('LOGIN MODE FINISHED')
            break
        else:
            print('you entered wrong login/password, try again')


def create_users_table(cursor):
    try:
        cursor.execute("""
        create table users(
        login TEXT UNIQUE,
        password_hash TEXT
        )
        """)
    except sqlite3.OperationalError as e:
        print(e)


def run():
    register()
    login()


if __name__ == '__main__':
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    create_users_table(cursor)

    run()

    conn.close()
