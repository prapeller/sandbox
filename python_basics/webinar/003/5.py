number_list = []


def spl_app_print_total(string_list):
    if string_list == '':
        print(f'Total sum of entered numbers = {sum(number_list)}\n')
    else:
        for number in string_list.split():
            try:
                number_list.append(float(number))
            except ValueError as e:
                print(e)
        print(f'Total sum of entered numbers = {sum(number_list)}\n')


while True:
    number_string = input('enter numbers separated by " "\n'
                          'press "Enter" to print sum\n'
                          'press "q" to quit > ')

    if 'q' in number_string:
        number_string_without_q = number_string.removesuffix('q')
        if number_string_without_q:
            spl_app_print_total(number_string_without_q)
        break
    else:
        spl_app_print_total(number_string)
