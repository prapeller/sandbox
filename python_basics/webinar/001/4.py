# через while
user_number = int(input('enter positive integer > '))
max_digit = 0

while user_number:
    next_digit = user_number % 10
    if next_digit > max_digit:
        max_digit = next_digit
    elif next_digit == 9:
        break
    user_number = user_number // 10

print(f'max digit of your integer: {max_digit}')

# наверное, более адекватное решение
user_number = input('enter positive integer > ')
max_digit = int(user_number[:1])

for digit in user_number:
    if int(digit) > max_digit:
        max_digit = int(digit)

print(f'max digit of your integer: {max_digit}')