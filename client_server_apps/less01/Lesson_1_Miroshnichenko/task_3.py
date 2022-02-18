"""
Задание 3.

Определить, какие из слов «attribute», «класс», «функция», «type»
невозможно записать в байтовом типе с помощью маркировки b'' (без encode decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
--- обязательно!!! усложните задачу, "отловив" и обработав исключение,
придумайте как это сделать
"""
eval_command_list = ["b'attribute'", "b'класс'", "b'функция'", "b'type'"]

for eval_command in eval_command_list:
    try:
        eval(eval_command)
    except SyntaxError as e:
        print(f'SyntaxError during command execution: "{eval_command}": {e}')
