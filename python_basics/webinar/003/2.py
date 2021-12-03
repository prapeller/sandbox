def print_user_data(name, surname, year_of_birth, place, email, tel):
    print(
        f'In {year_of_birth} was born {name} {surname}, '
        f'now this person lives in {place}, '
        f'with telephone number {tel}, '
        f'and email {email}.'
    )


print_user_data('Ivan', 'Petrov', tel='8-985-765-5302', email='email@email.ru', year_of_birth=1989, place='Moscow')
