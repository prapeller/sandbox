class Stationery:
    title = ''

    def draw(self):
        print('stationery draws')


class Pen(Stationery):
    def draw(self):
        print('pen draws')


class Pencil(Stationery):
    def draw(self):
        print('pencil draws')


class Handle(Stationery):
    def draw(self):
        print('handle draws')


pen = Pen()
pen.draw()

pencil = Pencil()
pencil.draw()

handle = Handle()
handle.draw()
