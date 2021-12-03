import json

positive_profit_firms_counter = 0
total_positive_profit = 0
firms_profit_dict = {}
average_profit_dict = {'average_profit': 0}

with open('7_file.txt', 'r', encoding='utf-8') as f:
    data = f.readlines()
    for line in data:
        line = line.replace('\n', '')
        line_list = line.split(' ')

        firm = line_list[0]
        proceeds = float(line_list[2])
        expenses = float(line_list[3])
        profit = proceeds - expenses
        firms_profit_dict[firm] = profit

        if profit >= 0:
            positive_profit_firms_counter += 1
            total_positive_profit += profit

average_profit = total_positive_profit / positive_profit_firms_counter
average_profit_dict['average_profit'] = average_profit

data_list = [firms_profit_dict, average_profit_dict]
print(data_list)

with open('7.json', 'w', encoding='utf-8') as f:
    json.dump(data_list, f)