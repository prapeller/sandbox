import itertools


def count_from_a_to_b(b):
    counter = itertools.count(3)
    while True:
        current = counter.__next__()
        print(current)
        if current == b:
            break


def cycle_of_list_n_times(n):
    cycle = itertools.cycle(['a', 'b', 'c'])
    counter = 1
    while True:
        current = cycle.__next__()
        print(current)
        counter += 1
        if counter > n:
            break


count_from_a_to_b(int(input('enter a number to count from 3 up to > ')))
cycle_of_list_n_times(int(input('enter number of times to iterate through "abc" > ')))
