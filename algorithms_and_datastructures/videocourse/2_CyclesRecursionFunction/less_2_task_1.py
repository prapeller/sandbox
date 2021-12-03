# 1. Написать программу, которая будет складывать, вычитать, умножать или делить два числа. Числа и знак операции
# вводятся пользователем. После выполнения вычисления программа не завершается, а запрашивает новые данные для
# вычислений. Завершение программы должно выполняться при вводе символа '0' в качестве знака операции. Если
# пользователь вводит неверный знак (не '0', '+', '-', '', '/'), программа должна сообщать об ошибке и снова
# запрашивать знак операции. Также она должна сообщать пользователю о невозможности деления на ноль, если он ввел
# его в качестве делителя.

# https://drive.google.com/file/d/1xLBsTXoCtTMOQJJzL7Ehn7QMYPNB4AhN/view?usp=sharing

oper = ''

while oper != '0':
    a = int(input('enter a'))
    b = int(input('enter b'))
    if b == 0:
        print('DivisionByZero error')
        continue

    while True:
        oper = input('enter operator... ')

        if oper == '0':
            break

        if oper != '+' and oper != '-' and oper != '*' and oper != '/':
            print('wrong operator')

        elif oper == '+':
            print(a + b)
            break
        elif oper == '-':
            print(a - b)
            break
        elif oper == '/':
            print(a / b)
            break
        else:
            print(a * b)
            break
