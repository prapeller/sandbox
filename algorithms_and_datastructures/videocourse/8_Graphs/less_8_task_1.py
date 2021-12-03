# 1. На улице встретились N друзей. Каждый пожал руку всем остальным друзьям (по одному разу). Сколько рукопожатий было?
# Примечание. Решите задачу при помощи построения графа.

graph = []

n = int(input('enter friends number: '))

# строим граф
for i in range(n):
    graph.append([1 for n in range(n)])
    graph[i][i] = 0

# выводим граф
print(*graph, sep='\n')

# выводим сумму рукопожатий
print(f'total handshakes: {sum(map(sum, graph))}')
