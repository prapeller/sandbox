import random
import math

random_list = [random.randint(-100, 100) for number in range(20)]
print(random_list)


def sqrt_if_positive_list(some_list):
    return [round(math.sqrt(number), 2) if number > 0 else number for number in some_list]


square_list = sqrt_if_positive_list(random_list)
print(random_list)
print(square_list)

