# 6. По длинам трех отрезков, введенных пользователем, определить возможность существования треугольника, составленного
# из этих отрезков. Если такой треугольник существует, то определить, является ли он разносторонним, равнобедренным или
# равносторонним.
# draw.io diagram:
# https://drive.google.com/file/d/1BuI_yelXvOaUGi5SUSD_Ces2tp8MnoA_/view?usp=sharing

a = int(input('enter length of triangle side 1... '))
b = int(input('enter length of triangle side 2... '))
c = int(input('enter length of triangle side 3... '))

if a >= (b + c) or b >= (a + c) or c >= (a + b):
    print(f'this triangle doesnt exists')
elif a == b == c:
    print('triangle is equilateral')
elif a == b or b == c or c == a:
    print('triangle is isosceles')
else:
    print('triangle is versatile')
