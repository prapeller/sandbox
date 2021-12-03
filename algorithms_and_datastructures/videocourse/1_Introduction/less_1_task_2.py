# 2. По введенным пользователем координатам двух точек вывести уравнение прямой вида y = kx + b,
# проходящей через эти точки.

# draw.io diagram:
# https://drive.google.com/file/d/1xFGZjhLOOi1X_nBzfAZ7DPtduFsjUas1/view?usp=sharing

print('enter A coordinates (x_1, y_1)... ')
x_1 = float(input('enter A x_1... '))
y_1 = float(input('enter A y_1... '))

print('enter B coordinates (x_2, y_2)... ')
x_2 = float(input('enter B x_2... '))
y_2 = float(input('enter B y_2... '))

if x_1 == x_2:
    print(f'x = {x_1:.2f}')

else:

    k = (y_1 - y_2) / (x_1 - x_2)
    b = y_2 - k * x_2

    if k == 0 and b != 0:
        print(f'y = {b:.2f}')
    elif k == 1 and b == 0:
        print(f'y = x')
    elif k != 0 and b == 0:
        print(f'y = {k:.2f}x')
    elif k != 0 and b > 0:
        print(f'y = {k:.2f}x + {b:.2f}')
    elif k != 0 and b < 0:
        print(f'y = {k:.2f}x {b:.2f}')
