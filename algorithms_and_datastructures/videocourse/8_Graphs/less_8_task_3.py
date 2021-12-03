# возвращает граф в котором все вершины связаны друг с другом
def make_connected_graph(ver_number):
    connected_graph = []
    for i in range(ver_number):
        connected_graph.append(list(range(ver_number)))
        del connected_graph[i][i]
    return connected_graph


# обходит все вершины графа начиная со стартовой
def visit_all_graph(g, s):
    visited = []

    def dfs(gr, st):
        visited.append(st)
        print(st)

        for neighbour in gr[st]:
            if neighbour not in visited:
                dfs(gr, neighbour)

    dfs(g, s)


one_graph = make_connected_graph(20)
another_graph = [
    [1, 3, 4, 6],
    [8, 0, 2, 4],
    [3, 7],
    [2, 5, 6, 7],
    [2],
    [3, 4, 6],
    [8, 3, 4, 5],
    [0, 8],
    [9, 5],
    [5]
]

visit_all_graph(one_graph, 0)
print()
visit_all_graph(another_graph, 0)
