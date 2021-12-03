import time
import logging

logging.basicConfig(format='%(levelname)s:%(message)s', filename='1.log', level=logging.DEBUG)


def write_log(color):
    logging.info(color)


def check():
    with open('1.log', 'rb') as f:
        f.seek(-35, 2)
        last_3_switches = f.read().decode()
        print(f'last 3 switches:\n{last_3_switches}')
        if last_3_switches.count('red') > 1 or \
                last_3_switches.count('yellow') > 1 or \
                last_3_switches.count('green') > 1:
            logging.fatal('error with switching')
            raise Exception
        else:
            print('checking status: OK')


class TrafficLight:
    __color = ''

    def __init__(self):
        self.__color = 'red'

    def running(self):
        switch_counter = 0

        while True:
            if self.__color == 'red':
                write_log(self.__color)
                print(self.__color)
                time.sleep(7)
                self.__color = 'yellow'
                switch_counter += 1
            elif self.__color == 'yellow':
                write_log(self.__color)
                print(self.__color)
                time.sleep(2)
                self.__color = 'green'
                switch_counter += 1
            elif self.__color == 'green':
                write_log(self.__color)
                print(self.__color)
                time.sleep(4)
                self.__color = 'red'
                switch_counter += 1

            if switch_counter > 2:
                check()
                switch_counter = 0


traffic_light = TrafficLight()
traffic_light.running()
