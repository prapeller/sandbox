user_input_list = input('enter expression, dividing words with " " sign > ').split()
for number, word in enumerate(user_input_list, 1):
    print(f'{number}) {word[:10]}')
