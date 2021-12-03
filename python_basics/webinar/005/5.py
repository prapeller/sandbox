import random


def create_file_with_numbers(file_name, numbers_qty, minim, maxim):
    with open(file_name, 'w', encoding='utf-8') as f:
        for _ in range(numbers_qty):
            f.write(str(random.randint(minim, maxim)) + ' ')


def calc_sum(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return sum([int(num_str) for num_str in f.read().split(' ') if num_str != ''])


create_file_with_numbers(file_name='5_file.txt', numbers_qty=5, minim=-20, maxim=20)
print(calc_sum('5_file.txt'))
