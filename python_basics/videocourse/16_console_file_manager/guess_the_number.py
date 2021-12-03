import random


def start_game():
    users = []
    levels_dict = {1: 10, 2: 5, 3: 3}
    computer_number = random.randint(0, 100)
    print(computer_number)
    user_guessed_number = None
    attempt_count = 0
    user_level = int(input('enter difficult level:\n' +
                           '1 - EASY, 10 attempts\n' +
                           '2 - NORMAL, 5 attempts\n' +
                           '3 - HARD, 3 attempts\n' +
                           '> '))
    max_attempt_count = levels_dict[user_level]

    user_count = int(input('enter number of users > '))
    for i in range(user_count):
        users.append(input(f'input user{i + 1} name > '))

    while computer_number != user_guessed_number:
        attempt_count += 1
        if max_attempt_count < attempt_count:
            print('attempts are out of limit, GAME OVER!')
            break
        print(f'try number {attempt_count}')

        for user in users:
            print(f"{user}'s move!")
            user_guessed_number = int(input('guess the number from 0 to 100 > '))
            if user_guessed_number > computer_number:
                print('number should be LESS!')
            elif user_guessed_number < computer_number:
                print('number should be MORE!')
            else:
                print(f'{user} is WINNER!')
                break
