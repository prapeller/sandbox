from functools import reduce

result = reduce(lambda i, j: i * j, [number for number in range(100, 1001, 2)])
print(result)
