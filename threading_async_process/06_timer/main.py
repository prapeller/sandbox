import os
import threading

dirname = os.path.dirname
base_dir = dirname(dirname(__file__))


def exec_watcher():
    timer = threading.Timer(1.0, print_files)
    timer.start()


def print_files():
    for i in os.listdir(base_dir):
        print(i)
    exec_watcher()


exec_watcher()
