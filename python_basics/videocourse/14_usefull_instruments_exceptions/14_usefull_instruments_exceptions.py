# has_name = True
has_name = False

name = 'Max' if has_name else 'no name'
print(name)

# is_one = True
is_one = False
number = 1 if is_one else 2
print(number)

# is_russian = True
is_russian = False
print('Привет мир' if is_russian else 'Hello world')

string = 'helloooooo'

# 1) lower/upper by if ilse
if_else_result = []

for i in range(len(string)):
    if i % 2 == 0:
        letter = string[i].upper()
        if_else_result.append(letter)
    else:
        letter = string[i].lower()
        if_else_result.append(letter)

result_string = ''.join(if_else_result)
print('1)', result_string)

# 2) lower/upper by ternar operator
ternar_result = []

for i in range(len(string)):
    letter = string[i]
    letter = letter.upper() if i % 2 == 0 else letter.lower()
    ternar_result.append(letter)

result_string = ''.join(ternar_result)
print('2)', result_string)


#

