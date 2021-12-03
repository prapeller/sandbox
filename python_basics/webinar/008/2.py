class MyDivisionByZeroException(Exception):
    def __init__(self, txt):
        self.txt = txt


def divide(a, b):
    if b == 0:
        raise MyDivisionByZeroException('!!!!!!!Zero!!!!!!! !!!!!!!!!Division!!!!!!! !!!!!!!!Error!!!!!!!!')
    else:
        return a / b


try:
    print(divide(8, 0))
except MyDivisionByZeroException as e:
    print(e)
else:
    print('divided ok!')
finally:
    print('tadaaaa!')
