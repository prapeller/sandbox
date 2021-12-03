def new_char_list(string, function):
    char_list = []
    for char in string:
        if function(char):
            char_list.append(char)
    return char_list


def new_char_set(string, function):
    char_list = []
    char_set = set(char_list)
    for char in string:
        if function(char):
            char_set.add(char)
    return char_set


vowel_list = ['a', 'e', 'i', 'o', 'u', 'y']
consonant_list = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']


def letter_is_vowel(letter):
    return letter in vowel_list


def letter_is_consonant(letter):
    return letter in consonant_list


string = 'hello'
string2 = 'hello'
print(new_char_list(string, letter_is_vowel))
print(new_char_list(string, lambda letter: letter in vowel_list))
print(new_char_set(string, lambda letter: letter in vowel_list))

print(new_char_list(string, letter_is_consonant))
print(new_char_list(string, lambda letter: letter in consonant_list))
print(new_char_set(string, lambda letter: letter in consonant_list))
