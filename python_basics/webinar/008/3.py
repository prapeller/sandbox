import re
digit_list = []


class NotDigitError(Exception):
    def __init__(self, text):
        self.txt = text


# 1 excepting ValueError
def append_to(user_list: list, value):
    try:
        user_list.append(float(value))
    except ValueError:
        raise NotDigitError('you entered not a number')


while True:
    user_input = input('enter number for adding to list > ')
    if user_input == 'stop':
        break

    try:
        append_to(digit_list, user_input)
    except NotDigitError as e:
        print(e)

print(digit_list)


# 2 excepting only my own exception
def to_float(value):
    regex = r"(\d+\.*\d*)"
    match = re.findall(regex, value)
    if not match:
        raise NotDigitError('you entered not a number')
    return float(value)


while True:
    user_input = input('enter number for adding to list > ')
    if user_input == 'stop':
        break

    try:
        digit_list.append(to_float(user_input))
    except NotDigitError as e:
        print(e)

print(digit_list)
