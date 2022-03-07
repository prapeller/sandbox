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


def test_time_check_not_changed():
    assert """def time_check(func):
    def wrapper(*args):
        start_time = time.time()
        result = func(*args)
        execution_time = round(time.time() - start_time, 1)
        print(f'Время выполнения функции: {execution_time} с.')
        return result""" in user_code, 'Не меняйте функцию time_check(func)'


def test_long_heavy_not_changed():
    assert """@time_check
@cache_args
def long_heavy(num):
    time.sleep(1)
    return num * 2""" in user_code, 'Не меняйте функцию long_heavy(num)'


def test_make_sure_cache_args_has_dict():
    search_str = re.search(r"(?<=cache_args)[\s\S]*(return)", user_code).group(0)
    assert '= {}' in search_str or '= dict()' in search_str, 'Убедитесь в том, что в функции cache_args обьявлен словарь для кэша.'


def test_check_output():
    assert """Время выполнения функции: 1.0 с.
2
Время выполнения функции: 0.0 с.
2
Время выполнения функции: 1.0 с.
4
Время выполнения функции: 0.0 с.
4
Время выполнения функции: 0.0 с.
4""" in output, 'Убедитесь в том, что вывод именно такой, как в комментах (первый вызов функции с одним и тем же параметром выполняется за 1.0 с., второй и последующие вызовы функции с тем же параметром за 0.0 с.'
