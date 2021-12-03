"""
Задание 6.
Задание на закрепление навыков работы с очередью

Реализуйте структуру "доска задач".

Структура должна предусматривать наличие несольких очередей задач, например,
1) базовой, откуда задачи берутся, решаются и отправляются в список решенных
2) очередь на доработку, когда нерешенные задачи из первой очереди отправляются
на корректировку решения

После реализации структуры, проверьте ее работу на различных сценариях

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.

Задание творческое. Здесь нет жестких требований к выполнению.
"""


class TaskQueue:

    def __init__(self):
        self.base_queue = []
        self.correction_queue = []
        self.finished_tasks = []

    def __repr__(self):
        return f'base_queue: {self.base_queue}\n' \
               f'correction_queue: {self.correction_queue}\n' \
               f'finished_tasks: {self.finished_tasks}'

    def is_empty(self):
        return True if (self.base_queue == [] and self.correction_queue == []) else False

    def to_queue(self, obj):
        self.base_queue.append(obj)

    def finish_task(self, from_base=True, from_correction=False):
        if from_correction:
            from_base = False
            task_to_finish = self.correction_queue.pop(0)
        if from_base:
            task_to_finish = self.base_queue.pop(0)
        self.finished_tasks.append(task_to_finish)

    def to_correction_queue(self):
        task_to_correction = self.base_queue.pop(0)
        self.correction_queue.append(task_to_correction)

    def clear_finished(self):
        self.finished_tasks.clear()


if __name__ == '__main__':
    task_queue = TaskQueue()

    task_queue.to_queue(1)
    task_queue.to_queue(2)
    task_queue.to_queue(3)
    print(f'is task queue empty?: {task_queue.is_empty()}')
    print(task_queue)
    print()

    task_queue.to_queue(4)
    task_queue.to_queue(5)
    task_queue.finish_task()
    task_queue.finish_task()
    task_queue.finish_task()
    task_queue.to_queue(6)
    task_queue.to_queue(7)
    task_queue.to_correction_queue()
    task_queue.to_correction_queue()
    task_queue.finish_task(from_correction=True)
    task_queue.finish_task(from_correction=True)
    task_queue.finish_task()
    task_queue.finish_task()

    print(f'is task queue empty?: {task_queue.is_empty()}')
    print(task_queue)
    print()

    task_queue.clear_finished()
    print(task_queue)
    print(f'is task queue empty?: {task_queue.is_empty()}')
