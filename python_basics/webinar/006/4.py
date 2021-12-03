class Car:
    color = ''
    name = ''
    speed = 0
    is_police = False

    def __init__(self, color, name):
        self.color = color
        self.name = name

    def go(self, speed):
        self.speed = speed
        print(f'{self.name} go with speed: {speed}!')

    def stop(self):
        self.speed = 0
        print(f'{self.name} stop!')

    def turn(self, direction):
        print(f'{self.name} turned to the {direction}!')

    def show_speed(self):
        print(f'speed: {self.speed}')


class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            print(f'speed: {self.speed}, slow down!')
        else:
            print(f'speed: {self.speed}')


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'speed: {self.speed}, slow down!')
        else:
            print(f'speed: {self.speed}')


class SportCar(Car):
    pass


class PoliceCar(Car):
    is_police = True


camry = TownCar('green', 'Toyota')
camry.show_speed()
camry.go(65)
camry.show_speed()
camry.turn('left')
camry.turn('right')
camry.speed = 59
camry.show_speed()
camry.stop()
camry.show_speed()
print(f'Is {camry.name} police car? {camry.is_police}!\n')

truck = WorkCar('black', 'Ford')
truck.show_speed()
truck.go(41)
truck.show_speed()
truck.turn('left')
truck.turn('right')
truck.speed = 39
truck.show_speed()
truck.stop()
truck.show_speed()
print(f'Is {truck.name} police car? {truck.is_police}!\n')

ferrari = SportCar('red', 'Ferrari')
ferrari.show_speed()
ferrari.go(200)
ferrari.show_speed()
ferrari.turn('left')
ferrari.turn('right')
ferrari.speed = 250
ferrari.show_speed()
ferrari.stop()
ferrari.show_speed()
print(f'Is {ferrari.name} police car? {ferrari.is_police}!\n')

cop = PoliceCar('blue-white', 'UAZ')
cop.show_speed()
cop.go(100)
cop.show_speed()
cop.turn('left')
cop.turn('right')
cop.stop()
cop.show_speed()
print(f'Is {cop.name} police car? {cop.is_police}!\n')
