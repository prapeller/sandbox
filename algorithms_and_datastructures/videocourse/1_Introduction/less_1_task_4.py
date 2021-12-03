# 4. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.

# draw.io diagram:
# https://drive.google.com/file/d/1iXiUEZipnr6iHIQqwdqxx3XiWHgrjwPr/view?usp=sharing
import re

char_1 = input('enter any character_1... ').lower()
char_2 = input('enter any character_2... ').lower()

regex_1 = '[a-z]'
regex_2 = '[а-я]'
char_1_match_eng = re.search(regex_1, char_1)
char_2_match_eng = re.search(regex_1, char_2)
char_1_match_rus = re.search(regex_2, char_1)
char_2_match_rus = re.search(regex_2, char_2)

if char_1_match_eng and char_2_match_eng:
    char_1_num = ord(char_1) - 96
    char_2_num = ord(char_2) - 96
    between_num = char_2_num - char_1_num - 1
    print(f'{char_1} stands at {char_1_num} alphabet place\n'
          f'{char_2} stands at {char_2_num} alphabet place\n'
          f'between "{char_1}" and "{char_2}" there are {abs(between_num)} characters')


elif char_1_match_rus and char_2_match_rus:
    char_1_num = ord(char_1) - 1071
    char_2_num = ord(char_2) - 1071
    between_num = char_2_num - char_1_num - 1
    print(f'{char_1} stands at {char_1_num} alphabet place\n'
          f'{char_2} stands at {char_2_num} alphabet place\n'
          f'between "{char_1}" and "{char_2}" there are {abs(between_num)} characters')

else:
    print('you entered characters from different alphabets')
