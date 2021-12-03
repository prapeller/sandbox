numbers = [2, 300, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

# обычным for думаю более читаемо
result = []
for i in range(1, len(numbers)):
    if numbers[i] > numbers[i - 1]:
        result.append(numbers[i])
print(result)

# list comprehension + range
result = [numbers[i] for i in range(1, len(numbers)) if numbers[i] > numbers[i - 1]]
print(result)

# generator expression + index
result = (n for n in numbers if numbers.index(n) > 0 and numbers[numbers.index(n)] > numbers[numbers.index(n) - 1])
print(list(result))
