def square_if_not_13(number):
    if number == 13:
        raise ValueError('unhappy number')
    return number ** 2


number = int(input('enter number from 1 to 100'))
try:
    result = square_if_not_13(number)
except ValueError as e:
    print('unhappy number :(')
else:
    print(result)
finally:
    print('this is the end')
