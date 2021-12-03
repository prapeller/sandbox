from sys import argv


def salary():
    try:
        rate, hours, bonus = map(float, argv[1:])
        print(f'salary = {hours * rate + bonus}')
    except Exception as e:
        print(e)
        print('enter the following arguments for calculating salary: rate, hours, bonus')


salary()
