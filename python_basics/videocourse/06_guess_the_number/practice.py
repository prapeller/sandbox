import random

print('ask yourself the number from 1 to 100')
min_number = 1
max_number = 100
user_reply = None

while user_reply != '=':
    guess_number = random.randint(min_number, max_number)
    print(f'that number was {guess_number}?')
    user_reply = input('type "<" if less, type ">" if more, type "=" is right... ')
    if user_reply == '<':
        max_number = guess_number - 1
    elif user_reply == '>':
        min_number = guess_number + 1
else:
    print(f'Hurray, your number was {guess_number}!')
