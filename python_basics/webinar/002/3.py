while True:
    try:
        user_month = int(input('enter month number from 1 to 12 > '))
        if 0 < user_month < 13:
            break
    except ValueError as e:
        continue

# 1) by list
seasons_list = [
    ['зима', [12, 1, 2]],
    ['весна', [3, 4, 5]],
    ['лето', [6, 7, 8]],
    ['осень', [9, 10, 11]]
]
for season in seasons_list:
    if user_month in season[1]:
        print(season[0])

# 2) by dict
seasons_dict = {
    'зима': [12, 1, 2],
    'весна': [3, 4, 5],
    'лето': [6, 7, 8],
    'осень': [9, 10, 11]
}
for season, month_number in seasons_dict.items():
    if user_month in month_number:
        print(season)
