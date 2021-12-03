class Date:
    def __init__(self, date_str: str):
        self.date_str = date_str

    @classmethod
    def date_str_to_int_list(cls, date_str: str):
        return list(map(int, date_str.split('-')))

    @classmethod
    def date_obj_to_int_list(cls, date_obj):
        return list(map(int, date_obj.date_str.split('-')))

    @staticmethod
    def check_is_valid_date_str(date_str: str):
        date_list = Date.date_str_to_int_list(date_str)
        return True if (0 < date_list[0] < 32) and (0 < date_list[1] < 13) and (date_list[2] > 0) else False

    @staticmethod
    def check_is_valid_date_obj(date_obj):
        date_list = Date.date_obj_to_int_list(date_obj)
        return True if (0 < date_list[0] < 32) and (0 < date_list[1] < 13) and (date_list[2] > 0) else False


# 2 числа в формате "число-месяц-год"
date_string = '13-09-1989'
date_string_2 = '32-02-1989'

# объект класса Date... по заданию не понятно использовать его в методах класса или нет
date_obj_1 = Date(date_string)
print(date_obj_1)
date_obj_2 = Date(date_string_2)
print(date_obj_2, '\n')

# без использования объекта (просто str)
date_list_1 = Date.date_str_to_int_list(date_string)
print(date_list_1)
print(f'date {date_string} is valid: {Date.check_is_valid_date_str(date_string)}')
date_list_2 = Date.date_str_to_int_list(date_string_2)
print(date_list_2)
print(f'date {date_string_2} is valid: {Date.check_is_valid_date_str(date_string_2)}\n')

# с использованием объекта
date_list_1 = Date.date_obj_to_int_list(date_obj_1)
print(date_list_1)
print(f'date {date_obj_1} is valid: {Date.check_is_valid_date_obj(date_obj_1)}')
date_list_2 = Date.date_obj_to_int_list(date_obj_2)
print(date_list_2)
print(f'date {date_obj_2} is valid: {Date.check_is_valid_date_obj(date_obj_2)}\n')
