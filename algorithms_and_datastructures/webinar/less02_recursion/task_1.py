"""
1.	Написать программу, которая будет складывать, вычитать, умножать или делить
два числа. Числа и знак операции вводятся пользователем. После выполнения
вычисления программа не должна завершаться, а должна запрашивать новые данные
для вычислений. Завершение программы должно выполняться при вводе символа '0'
в качестве знака операции. Если пользователь вводит неверный знак
(не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке и
снова запрашивать знак операции.

Также сообщать пользователю о невозможности деления на ноль,
если он ввел 0 в качестве делителя.

Подсказка:
Вариант исполнения:
- условие рекурсивного вызова - введена операция +, -, *, / - ШАГ РЕКУРСИИ
- условие завершения рекурсии - введена операция 0 - БАЗОВЫЙ СЛУЧАЙ

Пример:
Введите операцию (+, -, *, / или 0 для выхода): +
Введите первое число: 214
Введите второе число: 234
Ваш результат 448
Введите операцию (+, -, *, / или 0 для выхода): -
Введите первое число: вп
Вы вместо трехзначного числа ввели строку (((. Исправьтесь
Введите операцию (+, -, *, / или 0 для выхода):

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""


def run():
    sign = input('enter operation sign: +, -, *, /\n or 0 to quit > ')

    if sign == '0':
        return

    elif sign not in ('+', '-', '*', '/'):
        print('you entered wrong operation sign')
        run()

    else:
        try:
            a = int(input('enter a: (3 digit integer) > '))
            b = int(input('enter b: (3 digit integer) > '))

            if sign == '+':
                print(f'result: {a + b}')

            if sign == '-':
                print(f'result: {a - b}')

            if sign == '*':
                print(f'result: {a * b}')

            if sign == '/':
                print(f'result: {a / b}')

        except Exception as e:
            print(e)
        run()


if __name__ == '__main__':
    run()
