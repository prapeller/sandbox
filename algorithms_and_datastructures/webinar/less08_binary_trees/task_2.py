"""
Задание 2.

Доработайте пример структуры "дерево",
рассмотренный на уроке.

Предложите варианты доработки и оптимизации
(например, валидация значений узлов в соответствии с требованиями для бинарного дерева).

Поработайте с доработанной структурой, позапускайте на реальных данных - на клиентском коде.
"""


class CantPasteException(Exception):
    def __init__(self, message):
        super().__init__(message)


class BinaryTree:

    def __init__(self, root, left=None, right=None):
        self.root = root
        self.left = left
        self.right = right

    def set_root(self, obj):
        self.root = obj

    def get_root(self):
        return self.root

    def set_left(self, new_node):
        if new_node >= self.get_root():
            raise CantPasteException('left child should be less then root')

        if self.left is None:
            self.left = BinaryTree(new_node)
        else:
            tmp = BinaryTree(new_node)
            tmp.left = self.left
            self.left = tmp

    def get_left(self):
        return self.left

    def set_right(self, new_node):
        if new_node <= self.get_root():
            raise CantPasteException('right child should be more then root')

        if self.right is None:
            self.right = BinaryTree(new_node)
        else:
            tmp = BinaryTree(new_node)
            tmp.right = self.right
            self.right = tmp

    def get_right(self):
        return self.right

    def __repr__(self, res_str='', lvl=0):
        res_str = f'{self.root}'

        if lvl > 0:
            res_str = '\n' + (lvl - 1) * '\t' + '|__' + f'{self.root}'

        if self.left is None and self.right is None:
            return res_str

        if self.right and not self.left:
            res_str += self.right.__repr__(res_str=res_str, lvl=lvl + 1) + \
                       '\n' + '\t' * lvl + '|__None'

        if self.left and not self.right:
            res_str += '\n' + '\t' * lvl + '|__None' + \
                       self.left.__repr__(res_str=res_str, lvl=lvl + 1)

        if self.left and self.right:
            res_str += self.right.__repr__(res_str=res_str, lvl=lvl + 1) + \
                       self.left.__repr__(res_str=res_str, lvl=lvl + 1)

        return res_str


# создадим дерево, назначим корень 10
r = BinaryTree(10)
# попробуем назначить левого потомка не меньше чем корень
# r.set_left(11)
# __main__.CantPasteException: left child should be less then root

# назначим левого потомка 5, правого 15, посмотрим как выглядит дерево
r.set_left(5)
r.set_right(15)
# print(r)

"""
10          <корень
|__15           <правый потомок
|__5            <левый потомок
"""
# для левого 5 назначим левого 3 и правого 7, посмотрим как выглядит дерево
r.get_left().set_left(3)
r.get_left().set_right(7)
# print(r)
"""
10
|__15
|__5
	|__7
	|__3
"""

# для 15 назначим левого 12, посмотрим как выглядит дерево
r.get_right().set_left(12)
# print(r)

"""
10
|__15
	|__None
	|__12
|__5
	|__7
	|__3 
	
видим, что у правого есть только левый (12) а правого нет (None)
"""
# попробуем назначить для 15 правого меньше чем 15
# r.get_right().set_right(13)
# __main__.CantPasteException: right child should be more then root

# для 15 назначим правого 17
r.get_right().set_right(17)
# print(r)

"""
10
|__15               
	|__17
	|__12
|__5                
	|__7
	|__3
"""

# назначим 6 туда, где сейчас уже стоит 5 (левый от корня)
r.set_left(6)
# print(r)

"""
10
|__15
	|__17
	|__12
|__6
	|__None
	|__5
		|__7
		|__3 
		
видим, что весь бывший левый потомок (5 и его потомки) спустился и стал левым потомком нового узла, 
а правый потомок нового узла пока None 

попробуем вставить 5 вместо None и увидим ошибку
"""
# r.get_left().set_right(5)
# __main__.CantPasteException: right child should be more then root

r.get_left().set_right(50)
# print(r)
"""
10
|__15
	|__17
	|__12
|__6
	|__50
	|__5
		|__7
		|__3

а 50 вставилось
вроде дерево упорядочено, но не строго, ведь по факту, слева от корня 10 оказался больший потомок второго колена 50 
"""
