from itertools import count
import re


class OfficeEquipment:
    """
    Makes Office Equipment class instances with with following attributes:
    model, price, weight, measurements.
    Every created instance has its own ID.
    """

    _counter = count(0)

    def __init__(self, model, price, weight, measurements):
        self.model = model
        self.price = price
        self.weight = weight
        self.measurements = measurements
        self.id = next(self._counter)

    def __str__(self):
        return f'model: {self.model}, price: {self.price}, weight(kgs): {self.weight}, ' \
               f'measurements(mm): {self.measurements}'

    @staticmethod
    def print_hello():
        print('hello')

    @classmethod
    def print_created_ins_qty(cls):
        match = re.findall('[0-9]+', str(cls._counter))
        print(f'Office Equipment Class initialized the following instances quantity: {match[0]}\n')


class Printer(OfficeEquipment):
    def __init__(self, model, price, weight, measurements, printing_speed):
        super().__init__(model, price, weight, measurements)
        self.printing_speed = printing_speed


class Scanner(OfficeEquipment):
    def __init__(self, model, price, weight, measurements, scanning_speed):
        super().__init__(model, price, weight, measurements)
        self.scanning_speed = scanning_speed


class Copier(OfficeEquipment):
    def __init__(self, model, price, weight, measurements, xeroxing_speed):
        super().__init__(model, price, weight, measurements)
        self.xeroxing_speed = xeroxing_speed


class Warehouse:

    def __init__(self, name, address, square):
        self.name = name
        self.address = address
        self.square = square
        self.leftovers = {}
        self.shipment_counter = count(0)

    def __str__(self):
        return self.name

    def print_waybill(self, warehouse, *args):
        shp_num = re.findall('[0-9]+', str(self.shipment_counter))[0]
        with open(f'{self.name} - {warehouse.name} Waybill {shp_num}.txt', 'w', encoding='utf-8') as f:
            f.write(f'Shipment number: {shp_num}\n')
            f.write(f'from: {self.name} ({self.address})\n'
                    f'to: {warehouse.name} ({warehouse.address})\n\n')
            f.writelines([f'{arg.__class__.__name__} {arg.model:<20} {arg.price} rub\n' for arg in args])

    def accept(self, *args):
        for equipment in args:
            try:
                self.leftovers[f'{equipment.model}'][1].append(equipment)
                self.leftovers[f'{equipment.model}'][0] += 1
                print(f'{self.name} ({self.address} accepted {equipment})')
            except KeyError:
                print(f'{self.name} ({self.address}), registered new model: '
                      f'{equipment.__class__.__name__} {equipment.model}')
                self.leftovers[f'{equipment.model}'] = [1, [equipment]]
                print(f'{self.name} ({self.address} accepted {equipment})')
        print()

    def ship_equipment_obj(self, warehouse, *args):
        for equipment in args:
            print(f'{self.name} ({warehouse.address}) shipped {equipment} to {warehouse.name} ({warehouse.address})')
            self.leftovers[f'{equipment.model}'][0] -= 1
            self.leftovers[f'{equipment.model}'][1].remove(equipment)
            if self.leftovers[f'{equipment.model}'][0] < 1:
                print(f'{self.name} ({self.address}), is out of stock: '
                      f'{equipment.__class__.__name__} {equipment.model}')

        leftovers_copy = self.leftovers.copy()
        for key, value in self.leftovers.items():
            if not value[1]:
                leftovers_copy.pop(key)

        self.leftovers = leftovers_copy
        warehouse.accept(*args)

        self.shipment_counter.__next__()
        self.print_waybill(warehouse, *args)
        print()

    def ship_equipment_model(self, warehouse, equipment_type, qty):
        objs = []
        try:
            for key, value in self.leftovers.items():
                for i in range(qty):
                    if key == equipment_type:
                        objs.append(value[1][i])
            if not objs:
                print(f'can not ship {equipment_type} from {self.name}, it is out of stock!\n')
            else:
                self.ship_equipment_obj(warehouse, *objs)

        except TypeError as e:
            print(f'can not ship {equipment_type}, please enter quantity in digit format\n')

    def print_price_list(self):
        print(f'{self.name:<30} PRICE LIST {"=" * 10}')
        for key, value in self.leftovers.items():
            for obj in value[1]:
                print(f'{obj.__class__.__name__} {obj.model:<30} \t{obj.price} \trub')
            print('-' * 52)
        print()

    def print_leftovers(self):
        print(f'{self.name:<30} LEFTOVERS  {"=" * 10}')
        for key, value in self.leftovers.items():
            print(f'{value[1][0].__class__.__name__} {key:<30} \t{value[0]} \t\tpcs')
        print()


wh_1 = Warehouse('Main Warehouse', 'Moscow', 20)
wh_2 = Warehouse('Samara Department Warehouse', 'Samara', 10)

OfficeEquipment.print_hello()

printer_1 = Printer('HP Laser 107a', 7050, 5.58, [300, 220, 200], 20)
printer_2 = Printer('HP Laser 107a', 7000, 5.58, [300, 220, 200], 20)
printer_3 = Printer('Canon Pixma TS704', 5900, 8, [372, 365, 158], 15)
printer_4 = Printer('Canon Pixma TS704', 5926, 8, [372, 365, 158], 15)
printer_5 = Printer('HP Laser 107a', 7200, 5.58, [300, 220, 200], 20)
printer_6 = Printer('HP Laser 107a', 7300, 5.58, [300, 220, 200], 20)

copier_1 = Copier('Pantum M6500W', 10999, 9600, [417, 305, 244], 22)
copier_2 = Copier('Pantum M6500W', 11000, 9600, [417, 305, 244], 22)
copier_3 = Copier('Pantum M6500W', 12000, 9600, [417, 305, 244], 22)
copier_4 = Copier('Pantum M6500W', 10500, 9600, [417, 305, 244], 22)
copier_5 = Copier('Xerox B215', 8800, 14, [400, 400, 365], 30)
copier_6 = Copier('Xerox B215', 8890, 14, [400, 400, 365], 30)

scanner_1 = Scanner('Canon LiDE 300', 4990, 2.25, [250, 367, 42], 6)
scanner_2 = Scanner('Canon LiDE 300', 5000, 2.25, [250, 367, 42], 6)
scanner_3 = Scanner('Canon LiDE 300', 5100, 2.25, [250, 367, 42], 6)
scanner_4 = Scanner('Fujitsu fi-7160', 99500, 2.25, [300, 170, 163], 60)
scanner_5 = Scanner('Fujitsu fi-7160', 100000, 2.25, [300, 170, 163], 60)
scanner_6 = Scanner('Fujitsu fi-7160', 98300, 2.25, [300, 170, 163], 60)

OfficeEquipment.print_created_ins_qty()

wh_1.accept(printer_6, copier_2, printer_5, printer_1, printer_2, printer_3)
wh_1.accept(copier_1, printer_4, copier_3, copier_4, scanner_3, copier_6)
wh_1.accept(scanner_1, scanner_2, copier_5, scanner_4, scanner_5, scanner_6)

wh_1.print_leftovers()
wh_1.print_price_list()

wh_1.ship_equipment_obj(wh_2, printer_1, printer_2, printer_3, printer_4)

wh_1.print_leftovers()
wh_2.print_leftovers()

wh_1.ship_equipment_model(wh_2, 'HP Laser 107a', '2')
wh_1.ship_equipment_model(wh_2, 'HP Laser 107a', 2)
wh_1.ship_equipment_model(wh_2, 'HP Laser 107a', 1)
wh_2.ship_equipment_model(wh_1, 'HP Laser 107a', 1)
wh_1.ship_equipment_model(wh_2, 'Pantum M6500W', 3)
