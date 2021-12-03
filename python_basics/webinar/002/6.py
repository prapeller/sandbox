products_list = []
prop_dict = {'название': [], 'цена': [], 'количество': [], 'ед': [], 'производитель': []}

count = 0
while True:
    if input('press "Enter" to input goods properties, or any key to exit > ') != '':
        break
    count += 1
    good_tuple = (count, {})

    for prop in prop_dict.keys():
        user_input = input(f'enter {prop} > ')
        typed_input = int(user_input) if (prop == 'цена' or prop == 'количество') else user_input
        good_tuple[1][prop] = typed_input
        prop_dict[prop].append(typed_input)

    products_list.append(good_tuple)


print('структура данных:', products_list)
print(f'\n{"аналитика:":>17}')
for key, value in prop_dict.items():
    value = set(value)
    print(f'{key:>16}: {value}')
