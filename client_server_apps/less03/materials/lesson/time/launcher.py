"""Лаунчер"""

import os
import signal
import subprocess

PROCESS = []

while True:
    ACTION = input('Выберите действие: q - выход, '
                   's - запустить сервер и клиенты, x - закрыть все окна: ')

    if ACTION == 'q':
        break
    elif ACTION == 's':
        PROCESS.append(subprocess.Popen(args=('gnome-terminal', '--', 'python3', 'time_server.py'), stdout=subprocess.PIPE, preexec_fn=os.setsid))
        for i in range(5):
            PROCESS.append(subprocess.Popen(('gnome-terminal', '--', 'python3', 'time_client.py'), preexec_fn=os.setsid, stdout=subprocess.PIPE))
    elif ACTION == 'x':
        while PROCESS:
            VICTIM = PROCESS.pop()
            os.kill(os.getpgid(VICTIM.pid), signal.SIGKILL)
