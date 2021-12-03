data_dict = {}

with open('6_file.txt', 'r', encoding='utf-8') as f:
    data = f.readlines()
    for line in data:
        line = line.replace('(л)', '').replace('(пр)', '').replace('(лаб)', ''). \
            replace('—', '0').replace('-', '0').replace('\n', '').replace('.', '').replace(':', '')
        line_list = line.split(' ')
        discipline = line_list[0]
        hours = 0
        for i in range(1, len(line_list)):
            hour = line_list[i]
            hours += int(hour)
        if discipline:
            data_dict[discipline] = hours

print(data_dict)
