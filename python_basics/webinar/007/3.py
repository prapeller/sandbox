import textwrap


class Cell:
    def __init__(self, cells_qty):
        self.cells_qty = cells_qty

    def __add__(self, other):
        return Cell(self.cells_qty + other.cells_qty)

    def __sub__(self, other):
        if self.cells_qty > other.cells_qty:
            return Cell(self.cells_qty - other.cells_qty)
        else:
            print(f"{other} has less cells then {self}, can't subtract")
            return Cell(None)

    def __mul__(self, other):
        return Cell(self.cells_qty * other.cells_qty)

    def __truediv__(self, other):
        return Cell(round(self.cells_qty / other.cells_qty))

    def make_order(self, cell_in_a_row):
        cells_string = '*' * self.cells_qty
        return textwrap.fill(cells_string, cell_in_a_row)


cell_1 = Cell(30)
print(f'cell_1 cells quantity: {cell_1.cells_qty}')

cell_2 = Cell(100)
print(f'cell_2 cells quantity: {cell_2.cells_qty}')

cell_3 = cell_1 + cell_2
print(f'cell_3 cells quantity: {cell_3.cells_qty}')

cell_4 = cell_1 - cell_2
print(f'cell_4 cells quantity: {cell_4.cells_qty}')

cell_5 = cell_2 - cell_1
print(f'cell_5 cells quantity: {cell_5.cells_qty}')

cell_6 = cell_2 * cell_1
print(f'cell_6 cells quantity: {cell_6.cells_qty}')

cell_7 = cell_2 / cell_1
print(f'cell_6 cells quantity: {cell_7.cells_qty}')

cell_8 = cell_1 / cell_2
print(f'cell_6 cells quantity: {cell_8.cells_qty}')

print(Cell(12).make_order(5))
