def divide(num_1, num_2):
    try:
        return num_1 / num_2
    except Exception as e:
        print(e)


a = int(input('enter dividend > '))
b = int(input('enter divider > '))

print(divide(a, b))
