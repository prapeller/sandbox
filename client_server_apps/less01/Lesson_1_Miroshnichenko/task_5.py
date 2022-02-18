"""
Задание 5.

Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.

Подсказки:
--- используйте модуль chardet, иначе задание не засчитается!!!
"""

import subprocess
import threading

import chardet


class Command():
    def __init__(self, args, timeout):
        self.args = args
        self.timeout = timeout
        self.process = None

    def run(self):
        def target():
            print('Thread started')
            self.process = subprocess.Popen(self.args, stdout=subprocess.PIPE)
            for line in self.process.stdout:
                result = chardet.detect(line)
                print(result)
                line = line.decode(result['encoding']).encode('utf-8')
                print(line.decode('utf-8'))
            self.process.communicate()
            print('Thread finished')

        thread = threading.Thread(target=target)
        thread.start()
        thread.join(self.timeout)
        if thread.is_alive():
            print('terminating process...')
            self.process.terminate()
            thread.join()
        print(self.process.returncode)

args_1 = ['ping', 'yandex.ru']
args_2 = ['ping', 'youtube.com']

command_1 = Command(args_1, timeout=3)
command_2 = Command(args_2, timeout=3)

command_1.run()
command_2.run()



#
