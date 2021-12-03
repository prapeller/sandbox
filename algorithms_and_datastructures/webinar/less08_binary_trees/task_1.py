"""
Задание 1.
Реализуйте кодирование строки "по Хаффману".
У вас два пути:
1) тема идет тяжело? тогда вы можете, опираясь на пример с урока, сделать свою!!! версию алгоритма
Разрешается и приветствуется изменение имен переменных, выбор других коллекций, различные изменения
и оптимизации.

2) тема понятна? постарайтесь сделать свою реализацию.
Вы можете реализовать задачу, например, через ООП или предложить иной подход к решению.
"""

from collections import Counter, namedtuple
import heapq


class Node(namedtuple('Node', 'left, right, cnt, data', defaults=[None, None, 0, ''])):
    def __lt__(self, other):
        return self.cnt < other.cnt

    def walk(self, code_dic, node_repr):
        if len(self.data) < 2:
            code_dic[self.data] = node_repr or '0'
            return

        self.left.walk(code_dic, node_repr + '0')
        self.right.walk(code_dic, node_repr + '1')


def h_encode(s):
    """
    @param s: any string
    @return: dictionary {character: binary code} of string
    """
    code = {}
    h = [(cnt, Node(cnt=cnt, data=ch)) for ch, cnt in Counter(s).items()]
    if h:
        heapq.heapify(h)
    else:
        return code

    while len(h) > 1:
        cnt_l, left = heapq.heappop(h)
        cnt_r, right = heapq.heappop(h)
        cnt, node = cnt_l + cnt_r, Node(cnt=cnt_l + cnt_r, data=left.data + right.data, left=left, right=right)
        heapq.heappush(h, (cnt, node))

    [(_cnt, root)] = h
    root.walk(code, '')

    return code


def run():
    s = input('enter string to encode > ')
    code_dict = h_encode(s)
    print(code_dict)
    res = ''.join(code_dict[char] for char in s)
    print(res)


if __name__ == '__main__':
    run()
