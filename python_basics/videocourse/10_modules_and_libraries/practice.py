import os
import random


# 1
def create_dir():
    for i in range(1, 10):
        os.mkdir(f'dir_{i}')


def delete_dir():
    for i in range(1, 10):
        os.rmdir(f'dir_{i}')


# create_dir()
# delete_dir()


# 2
def get_random_from_list(lst):
    if lst:
        return random.choice(lst)


if __name__ == '__main__':
    print(get_random_from_list([1, 2, 3, 4]))
    print(get_random_from_list([]))
