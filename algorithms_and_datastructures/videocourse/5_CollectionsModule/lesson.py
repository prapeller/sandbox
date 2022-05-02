# from collections import Counter
#
# a = Counter()
# b = Counter('abrakadabra')
# c = Counter({'red': 2, 'blue': 4})
# d = Counter(cats=4, dogs=5)
# e = Counter(a=3, b=3, c=0, d=4)
# f = Counter(a=1, b=2, c=3, d=-4)

# print(a, b, c, d, sep='\n')

# print(b['z'])
# b['z'] = 1
# print(b)
# print(b['z'])
# print(list(b.elements()))
# b['z'] = 0
# print(list(b.elements()))
# print(b.most_common())
# print(b.most_common(2))
#
# print(e)
# e.subtract(f)
# print(e)
# print(set(e))
# print(dict(e))
# e.clear()
# print(e)
# print()
#
# print(f'{e} + {f} = {e + f}')
# print(f'{e} - {f} = {e - f}')
#
# print(e & f)
# print(e | f)
# print(+f)
# print(-f)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# from collections import deque

# a = deque()
# b = deque('abcde')
# c = deque([1, 2, 3, 4, 5])
#
# print(a, b, c, sep='\n')
#
# print(deque(c, maxlen=3))
# print(deque(c, 3))
#
# c.clear()
# print(c)

# d = deque([n for n in range(5)])
# print(d)
# d.append(5)
# print(d)
# d.appendleft(-1)
# print(d)
#
# d.extend([6, 7, 8])
# print(d)
# d.extendleft([-2, -3, -4])
# print(d)
# d = deque(d, 7)
# print(d)
#
# x = d.pop()
# print(d, x)
#
# y = d.popleft()
# print(d, y)
#
# print(d.count(7))
# print(d.index(7))
# print()
#
# d.insert(0, 2)
# d.insert(d.index(7)+1, 8)
# print(d)
# print()
#
# d.rotate(2)
# print(d)
# d.reverse()
# print(d)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

from collections import defaultdict

# a = defaultdict()
# print(a)
#
# s = 'lkajshdfkajoiashdofasdhfaosidnfaoishgadfakjdbuob'
# b = defaultdict(int)
# for char in s:
#     b[char] += 1
#
# print(b)

# data_list = [('cat', 1), ('dog', 5), ('cat', 2), ('mouse', 1), ('dog', 1), ('dog', 1), ('dog', 5)]
# c = defaultdict(int)
# for k, v in data_list:
#     c[k] += 1
# print(c)
#
# data_list = [('cat', 1), ('dog', 5), ('cat', 2), ('mouse', 1), ('dog', 1), ('dog', 1), ('dog', 5)]
# d = defaultdict(list)
# for k, v in data_list:
#     d[k].append(v)
# print(d)
#
# data_list = [('cat', 1), ('dog', 5), ('cat', 2), ('mouse', 1), ('dog', 1), ('dog', 1), ('dog', 5)]
# e = defaultdict(set)
# for k, v in data_list:
#     e[k].add(v)
# print(e)
#
# f = defaultdict(lambda: 'unknown')
# f.update(rex='dog', tomas='cat')
# print(f)
# print(f['rex'])
# print(f['jerry'])

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

from collections import OrderedDict

# a = {'cat': 5, 'mouse': 4, 'dog': 2}
# b = {'mouse': 4, 'cat': 5, 'dog': 2}
# print(a)
# print(b)
# print(a == b)
# print()
#
# ordered_a = OrderedDict(a)
# ordered_b = OrderedDict(b)
# print(ordered_a == ordered_b)
#
#
# sorted_by_key = sorted(a.items(), key=lambda x: x[0])
# print(sorted_by_key)
# print()
#
# sorted_by_value = sorted(a.items(), key=lambda x: x[1])
# print(sorted_by_value)
# print()
#
# print(sorted_by_key == sorted_by_value)
# print()
#
# ordered = OrderedDict(a)
# print(f"OrderedDict from {a}: {ordered}")
# ordered.move_to_end('mouse', last=True)
# print(ordered)
# print()

# ordered = OrderedDict(a)
# print(ordered)
# ordered.move_to_end('mouse', last=False)
# print(ordered)
# ordered.move_to_end('mouse', last=True)
# print(ordered)
# print()
#
# print('adding value to non existing key in OrderedDict')
# ordered['cow'] = 1
# print(ordered)
# ordered['cat'] = 1
# print(ordered)
#
# abd_dict = {'booooooom': 4, 'boom': 2, 'booooom': 3, 'booom': 1, 'boooooooooooom': 5}
# #
# sorted_by_key_length_list = sorted(abd_dict.items())
# print(sorted_by_key_length_list)
# sorted_by_value_list = sorted(abd_dict.items(), key=lambda x: x[1])
# print(sorted_by_value_list)
#
# reversed_list = reversed(sorted_by_key_length_list)
# print(list(reversed_list))
#
# ordered_by_value_dict = OrderedDict(sorted(abd_dict.items(), key=lambda x: x[1]))
# print(ordered_by_value_dict)
# ordered_by_value_dict['booooooooooooooooooooooooom'] = 4
# print(ordered_by_value_dict)
# ordered_by_value_dict['bom'] = -1
# print(ordered_by_value_dict)
# ordered_by_value_dict.move_to_end('bom', last=False)
# print(ordered_by_value_dict)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
from collections import namedtuple
#
# hero_1 = ('hero_1', 'troll', 100, 0.0, 250)
# print(hero_1)
# print(hero_1[1])
#
# Hero = namedtuple('Hero', 'name, race, health, mana, strength')
# hero_2 = Hero('hero_2', 'troll', 100, 0.0, 250)
# print(hero_2)
# print(hero_2.race)
#
# hero_3 = Hero('hero_3', 'human', strength=100, mana=20, health=90)
# print(hero_3)
# print(hero_3.race)
# print()
#
# characteristics = ['bot', 'orc', 200, 200, 5]
# bot_1 = Hero._make(characteristics)
# print(bot_1)
# print(bot_1.race)
# print()
# #
# bot_1_ordered_dict = bot_1._asdict()
# print(bot_1_ordered_dict)
# print(bot_1_ordered_dict['race'])
# print()
# #
# bot_2 = bot_1._replace(race='undead')
# print(bot_2)
# print(bot_2.race)
# print(bot_2._fields)
# print()
#
# Hero = namedtuple('Hero', 'name, race, health, mana, strength', defaults=[None, None, 100, 10, 0])
# hero_4 = Hero(name='Uroc')
# print(hero_4)
# print(hero_4._field_defaults)
# print(hero_4.race)
# print()
#
# characteristics_2 = {'health': 100, 'mana': 50, 'strength': 200}
# hero_5 = Hero('player2', 'wizard', **characteristics_2)
# print(hero_5)
# print(hero_5.race)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

from collections import ChainMap
#
# d_1 = {'a': 2, 'b': 4, 'c': 6}
# d_2 = {'a': 10, 'b': 20, 'd': 40}
#
# print(d_1, d_2)
# d_map = ChainMap(d_1, d_2)
# print(d_map)
# print()
#
# d_1['a'] = 4
# print(d_map)
#
# print(d_map['a'])
# print(d_map['d'])
# print()
#
# d_map_with_child = d_map.new_child({'a': 0, 'b': 0, 'c': 0})
# print(d_map_with_child)
# d_map_with_empty_child = d_map_with_child.new_child()
# print(d_map_with_empty_child)
# print()
#
# print(d_map_with_empty_child.maps)
# print(d_map_with_empty_child.maps[0])
# print(d_map_with_empty_child.maps[1])
# print(d_map_with_empty_child.maps[2])
# print(d_map_with_empty_child.maps[-1])
# print()
#
# print(d_map_with_empty_child)
# print(d_map_with_empty_child.parents)
# print(list(d_map_with_empty_child))
# print(list(d_map_with_empty_child.values()))

enclosed
composition/aggregation