proceeds = int(input('enter company proceeds > '))
costs = int(input('enter company costs > '))
result = proceeds - costs

if result > 0:
    print(f'company is profitable, result: {result}')
    is_profitable = True
    print(f'profitability: {result/proceeds}')
    employees_number = int(input('enter the number of employees > '))
    print(f'profit per 1 employee: {result / employees_number}')
else:
    print(f'company is not profitable, result {result}')