"""
Задание 5.
Задание на закрепление навыков работы со стеком

Реализуйте структуру "стопка тарелок".

Мы можем складывать тарелки в стопку и при превышении некоторого значения
нужно начать складывать тарелки в новую стопку.

Структура должна предусматривать наличие нескольких стеков.
Создание нового стека происходит при достижении предыдущим стеком порогового значения.
Реализуйте по аналогии с примером, рассмотренным на уроке, необходимые методы,
для реализации это структуры, добавьте новые методы (не рассмотренные в примере с урока)
для реализации этой задачи.

После реализации структуры, проверьте ее работу на различных сценариях

Подсказка:
Отдельне стопки можно реализовать через:
1) созд-е экземпляров стека (если стопка - класс)
или
2) lst = [[], [], [], [],....]

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.

Задание творческое. Здесь нет жестких требований к выполнению.
"""


class PlateStacks:
    def __init__(self, stacks_qty, max_plate_qty):
        self.plate_stacks = [[] for _ in range(stacks_qty)]
        self.max_plate_qty = max_plate_qty

    def __repr__(self):
        result_string = ''
        for stack in self.plate_stacks:
            result_string += str(stack) + '\n'
        return result_string

    def is_empty(self):
        for current_stack in self.plate_stacks:
            if not current_stack:
                continue
            else:
                return False
        return True

    def push_in(self, el):
        for current_stack in self.plate_stacks:
            if len(current_stack) < self.max_plate_qty:
                current_stack.append(el)
                return
            else:
                continue
        raise IndexError(f'PlateStacks is full!')

    def pop_out(self):
        for current_stack in reversed(self.plate_stacks):
            if not current_stack:
                continue
            else:
                return current_stack.pop()
        raise IndexError(f'pop out form empty PlateStacks!')

    def get_val(self):
        for current_stack in reversed(self.plate_stacks):
            if not current_stack:
                continue
            else:
                return current_stack[len(current_stack) - 1]

    def get_size(self):
        for current_stack in self.plate_stacks:
            if len(current_stack) > self.max_plate_qty:
                continue
            return len(current_stack)


if __name__ == '__main__':

    # create simple instance of PlateStacks() with stacks quantity = 3, max plate quantity (in every stack) = 3
    plate_stacks = PlateStacks(3, 3)

    # push in until its full
    plate_stacks.push_in(1)
    plate_stacks.push_in(2)
    print(f'added 2 objects, the last one: {plate_stacks.get_val()}')
    print(f'size of current stack: {plate_stacks.get_size()}')
    plate_stacks.push_in(3)
    plate_stacks.push_in(4)
    plate_stacks.push_in(5)
    plate_stacks.push_in(6)
    plate_stacks.push_in(7)
    plate_stacks.push_in(8)
    plate_stacks.push_in(9)
    print(f'added 9 objects, the last one: {plate_stacks.get_val()}')
    print(f'size of current stack: {plate_stacks.get_size()}')

    try:
        plate_stacks.push_in(10)
    except IndexError:
        print('oops, you are trying to push in, but all stacks are full!')
    print(plate_stacks)

    print(f'are plate stacks empty? {plate_stacks.is_empty()}')

    # pop out until its empty
    plate_stacks.pop_out()
    plate_stacks.pop_out()
    plate_stacks.pop_out()
    plate_stacks.pop_out()
    plate_stacks.pop_out()
    plate_stacks.pop_out()
    plate_stacks.pop_out()
    plate_stacks.pop_out()
    plate_stacks.pop_out()

    try:
        plate_stacks.pop_out()
    except IndexError:
        print('oops, you are trying to pop out, but all stacks are empty!')

    print(f'are plate stacks empty? {plate_stacks.is_empty()}')

    print(plate_stacks)
