import io
from contextlib import redirect_stdout

from precode import *

# file_path = 'author.py'
file_path = 'precode.py'

try:
    with open(file_path, encoding='utf-8') as f:
        user_code = f.read()

    with io.StringIO() as buf, redirect_stdout(buf):
        exec(user_code)
        output = buf.getvalue()
except Exception as e:
    print(e)


def test_show_contact_presence():
    assert 'def show_contact(self):' in user_code, f'Убедитесь в том, что метод show_contact объявлен'


def test_mike_show_contact():
    assert 'mike.show_contact()' in user_code, f'Обратитесь к методу show_contact() объекта mike'


def test_show_all_attrs():
    assert all(
        attr in output for attr in mike.__dict__.values()
    ), f'Убедитесь в том, что метод show_contact() выводит все свойства класса Contact'


def test_vlad_show_contact():
    assert 'vlad.show_contact()' in user_code, f'Обратитесь к методу show_contact() объекта vlad'


def test_print_contact_removed():
    assert 'def print_contact():' not in user_code, f'Удалите из кода функцию print_contact().'
