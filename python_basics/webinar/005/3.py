with open('3_employees_list.csv', encoding='utf-8') as f:
    total_salary = 0
    employees_counter = 0
    for line in f.readlines():
        data = line.split(',')
        total_salary += int(data[1])
        employees_counter += 1
        if int(data[1]) < 20000:
            print(f'Salary < 20000 has the following: {data[0]}')
    print(f'Average employees salary:         {round(total_salary / employees_counter, 2)}')
