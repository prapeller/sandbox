import re
from contextlib import redirect_stdout
import io

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


def test_div2_not_changed():
    assert 'div2 = make_divider_of(2)' in user_code, 'Убедитесь в том, что в объявление переменной div2 не менялось вами.'


def test_div2_print_not_changed():
    assert 'print(div2(10))' in user_code, 'Убедитесь в том, что вывод print(div2(10)) не менялось вами.'


def test_div5_not_changed():
    assert 'div5 = make_divider_of(5)' in user_code, 'Убедитесь в том, что в объявление переменной div5 не менялось вами.'


def test_div5_print_not_changed():
    assert 'print(div5(20))' in user_code, 'Убедитесь в том, что вывод print(div5(20)) не менялось вами.'


def test_make_divider_of_not_changed():
    assert """def make_divider_of(divider):
    def division_operation(divisible):""" in user_code, 'Убедитесь в том, что объявление функции make_divider_of и вложенной в нее функции division_operation не менялось вами.'

def test_check_output():
    assert """5.0
4.0
2.0""" in output, 'Убедитесь в том, что вывод именно такой, как в комментах:\n' \
                '5.0\n' \
                '4.0\n' \
                '2.0'
