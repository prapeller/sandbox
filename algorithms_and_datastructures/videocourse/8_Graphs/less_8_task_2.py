# 2. Доработать алгоритм Дейкстры (рассматривался на уроке), чтобы он дополнительно возвращал список вершин, которые
# необходимо обойти.
#
# это взрыв мозга... 2 дня сидел смотрел в моник на дебагер, и только на 3й день понял зачем нужен был parent list,
# который в этой реализации я переименовал в 'came_from', так как родитель с течением алгоритма может скорректироваться
# на более оптимальный родитель, то решил вот так переименовать, для удобства собственного восприятия...
# тут алгоритм Дейкстры дополнительно возвращает словарь с ключом-вершиной и значением-списком обойденных до этого ключа
# вершин


from collections import deque

g = [
    [0, 0, 1, 1, 9, 0, 0, 0],
    [0, 0, 9, 4, 0, 0, 7, 0],
    [0, 9, 0, 0, 3, 0, 6, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 5, 0],
    [0, 0, 7, 0, 8, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 2, 0],
]


def dijkstra(graph, start):
    ver_qty = len(graph)
    is_visited = [False] * ver_qty
    cost_list = [float('inf')] * ver_qty
    came_from = [None] * ver_qty

    current = start
    cost_list[current] = 0
    came_from[current] = current
    min_cost_to_current = 0

    tracking_dict = {i: None for i in range(ver_qty)}

    while min_cost_to_current < float('inf'):
        is_visited[current] = True

        for to_ver, cost in enumerate(graph[current]):

            if not is_visited[to_ver] and cost > 0:
                old_cost = cost_list[to_ver]
                new_cost = cost + cost_list[current]
                if new_cost < old_cost:

                    cost_list[to_ver] = new_cost
                    came_from[to_ver] = current

        min_cost_to_current = float('inf')

        # from which start next?
        for j in range(ver_qty):
            if cost_list[j] < min_cost_to_current and not is_visited[j]:
                min_cost_to_current = cost_list[j]
                current = j

    # based on 'came_from' list - filling tracking dict
    for i, previous in enumerate(came_from):
        if previous is None:
            continue
        before = came_from[i]
        que = deque([before])
        while before != start:
            before = came_from[before]
            que.appendleft(before)

        if i not in que:
            que.append(i)
        tracking_dict[i] = list(que)

    # printing tracking_dict
    # print(*tracking_dict.items(),  sep='\n')
    # print()
    return cost_list, tracking_dict


s = int(input('enter start point: '))
print(*dijkstra(g, s), sep='\n\n')
