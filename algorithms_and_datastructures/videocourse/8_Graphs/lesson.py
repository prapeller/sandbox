# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
from collections import namedtuple
from collections import deque

# non_directed_adjacency_matrix = [
#     [0, 1, 1, 0],
#     [1, 0, 1, 1],
#     [1, 1, 0, 0],
#     [0, 1, 0, 0],
# ]
#
# directed_graph_adjacency_matrix = [
#     [0, 1, 1, 0],
#     [0, 0, 1, 1],
#     [0, 1, 0, 0],
#     [0, 0, 0, 0],
# ]
#
#
# weighted_directed_graph_adjacency_matrix = [
#     [0, 2, 3, 0],
#     [0, 0, 2, 1],
#     [0, 2, 0, 0],
#     [0, 0, 0, 0],
# ]

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# # adjacency_list ******* список смежности
# graph = []
# graph.append([1, 2])
# graph.append([0, 2, 3])
# graph.append([0, 1])
# graph.append([1])
# print(graph, end='\n\n')
# print(*graph, sep='\n')

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# # adjacency_list as dict ******* список смежности в виде словаря
# graph_2 = {
#     0: {1, 2},
#     1: {0, 2, 3},
#     2: {0, 1},
#     3: {1},
# }
# print(graph_2)
# print(True if 3 in graph_2[1] else False)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# # adjacency_list as dict *******  всзвешенного графа в виде списка смежности как именованный словарь
# Vertex = namedtuple('Vertex', ['vertex', 'edge'])
# graph_3 = []
# graph_3.append([Vertex(1, 2), Vertex(2, 3)])
# graph_3.append([Vertex(0, 2), Vertex(2, 2), Vertex(3, 1)])
# graph_3.append([Vertex(0, 3), Vertex(1, 2)])
# graph_3.append([Vertex(1, 1)])
# print(*graph_3, sep='\n')
# for v in graph_3[1]:
#     if v.vertex == 3:
#         print(True)
#
# print(True if 3 in [v.vertex for v in graph_3[1]] else False)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# # adjacency_list as dict *******  всзвешенного графа в виде списка смежности как класс
# class Graph:
#     def __init__(self, vertex, edge):
#         self.vertex = vertex
#         self.edge = edge
#         # self.spam = spam

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# # edge list **** список ребер
# graph = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 1)]
#
# print(*graph, sep='\n')




# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Breadth-First Search

# g = [
#     [0, 1, 0, 0],
#     [1, 0, 1, 1],
#     [0, 1, 0, 1],
#     [0, 1, 1, 0],
# ]
#
# g = [
#     [0, 1, 1, 0, 1, 0, 0, 0],
#     [1, 0, 0, 0, 0, 0, 0, 0],
#     [1, 0, 0, 0, 1, 0, 0, 0],
#     [0, 0, 0, 0, 0, 1, 0, 0],
#     [1, 0, 1, 0, 0, 0, 1, 0],
#     [0, 0, 0, 1, 0, 0, 1, 1],
#     [0, 0, 0, 0, 1, 1, 0, 1],
#     [0, 0, 0, 0, 0, 1, 1, 0],
# ]
#
#
# def bfs(graph, start, finish):
#     from_whom = [None for _ in range(len(graph))]
#     is_visited = [False for _ in range(len(graph))]
#
#     check_que = deque([start])
#     is_visited[start] = True
#
#     while len(check_que) > 0:
#         current = check_que.pop()
#         if current == finish:
#             break
#
#         for i in range(len(graph[current])):
#             is_visible = True if graph[current][i] == 1 else False
#             is_not_visited = not is_visited[i]
#             if is_visible and is_not_visited:
#                 is_visited[i] = True
#                 from_whom[i] = current
#                 check_que.appendleft(i)
#     else:
#         return f'theres no way from {start} to {finish}'
#
#     cost = 0
#     way = deque([finish])
#     i = finish
#     while from_whom[i] != start:
#         cost += 1
#         way.appendleft(from_whom[i])
#         i = from_whom[i]
#
#     cost += 1
#     way.appendleft(start)
#     return f'the shortest way: {list(way)} with length {cost} points'
#
#
# lst = bfs(g, 0, 5)
# print(lst)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


# g = [
#     [0, 0, 1, 1, 9, 0, 0, 0],
#     [0, 0, 9, 4, 0, 0, 7, 0],
#     [0, 9, 0, 0, 3, 0, 6, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 1, 0],
#     [0, 0, 0, 0, 0, 0, 5, 0],
#     [0, 0, 7, 0, 8, 1, 0, 0],
#     [0, 0, 0, 0, 0, 1, 2, 0],
# ]
#
#
# def dijkstra(graph, start):
#     length = len(graph)
#     is_visited = [False] * length
#     cost = [float('inf')] * length
#     parent = [-1] * length
#
#     cost[start] = 0
#     min_cost = 0
#
#     while min_cost < float('inf'):
#         is_visited[start] = True
#
#         for i, vertex in enumerate(graph[start]):
#             if vertex != 0 and not is_visited[i]:
#
#                 if cost[i] > vertex + cost[start]:
#                     cost[i] = vertex + cost[start]
#                     parent[i] = start
#
#         min_cost = float('inf')
#         for i in range(length):
#             if min_cost > cost[i] and not is_visited[i]:
#                 min_cost = cost[i]
#                 start = i
#
#     return cost
#
#
# s = 0
# print(dijkstra(g, s))

