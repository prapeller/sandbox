import random

list_1 = (random.randint(-500, 500) for number in range(20))
list_1 = list(list_1)
print(list_1)

list_2 = [number for number in list_1 if number % 3 == 0 and number > 0 and number % 4 != 0]
print(list_2)