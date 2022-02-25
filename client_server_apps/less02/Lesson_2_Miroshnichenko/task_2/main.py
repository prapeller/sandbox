"""
2. Задание на закрепление знаний по модулю json. Есть файл orders
в формате JSON с информацией о заказах. Написать скрипт, автоматизирующий
его заполнение данными.

Для этого:
Создать функцию write_order_to_json(), в которую передается
5 параметров — товар (item), количество (quantity), цена (price),
покупатель (buyer), дата (date). Функция должна предусматривать запись
данных в виде словаря в файл orders.json. При записи данных указать
величину отступа в 4 пробельных символа;
Проверить работу программы через вызов функции write_order_to_json()
с передачей в нее значений каждого параметра.

ПРОШУ ВАС НЕ УДАЛЯТЬ ИСХОДНЫЙ JSON-ФАЙЛ
ПРИМЕР ТОГО, ЧТО ДОЛЖНО ПОЛУЧИТЬСЯ

{
    "orders": [
        {
            "item": "printer",
            "quantity": "10",
            "price": "6700",
            "buyer": "Ivanov I.I.",
            "date": "24.09.2017"
        },
        {
            "item": "scaner",
            "quantity": "20",
            "price": "10000",
            "buyer": "Petrov P.P.",
            "date": "11.01.2018"
        }
    ]
}

вам нужно подгрузить JSON-объект
и достучаться до списка, который и нужно пополнять
а потом сохранять все в файл
"""
import datetime
import json


def write_order_to_json(item, quantity, price, buyer, date, file_name='orders.json'):
    with open(file_name, 'r', encoding='utf-8') as f:
        data_dict = json.load(f)
    with open(file_name, 'w', encoding='utf-8') as f:
        orders_list = data_dict.get('orders')
        orders_list.append({
            'item': item,
            'quantity': quantity,
            'price': price,
            'buyer': buyer,
            'date': date,
        })
        json.dump(data_dict, f, indent=4)


write_order_to_json('item1', 100, 200.20, 'buyer1', str(datetime.datetime.now()))
write_order_to_json('item2', 100, 200.20, 'buyer2', str(datetime.datetime.now()))
write_order_to_json('item3', 100, 200.20, 'buyer3', str(datetime.datetime.now()))
