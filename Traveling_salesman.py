# python3
import itertools

Max_t = 10 ** 9
def sol(path_weight, path):
    print(path_weight)
    if path_weight == -1:
        return
    print(' '.join(map(str, path)))


def opt(graph):
    n = len(graph)
    depth = [[Max_t] * n for _ in range(2 ** n)]
    depth[1][0] = 0
    for s in range(2, n + 1):
        for subset in get_size(s, n):
            numeric_subset = get_value(subset)  # transforming subset in number
            depth[numeric_subset][0] = Max_t
            for i in subset:
                if i != 0:
                    minimum = Max_t
                    for j in subset:
                        if j != i:
                            minimum = min(minimum, depth[numeric_subset ^ (1 << i)][j] + graph[i][j])
                    depth[numeric_subset][i] = minimum
    result = Max_t
    for i in range(0, n):
        if i != 0:
            result = min(result, depth[2 ** n - 1][i] + graph[i][0])
    edges = []
    if result == Max_t:
        return -1, edges
    backward(depth, edges, 2 ** n - 1, 0, graph)
    return result, edges

def get_size(s, n):
    return [x + (0,) for x in itertools.combinations(range(1, n), s - 1)]

def get_value(subset):
    value = 0
    for x in subset:
        value += 2 ** x
    return value

def backward(depth, edges, numeric_subset, to, graph):
    subset = bin(numeric_subset).split('b')[1][::-1]
    subset = construct(subset)
    index = 0
    mini = Max_t
    for i in subset:
        if i != to:
            if depth[numeric_subset][i] + graph[i][to] < mini:
                index = i
                mini = depth[numeric_subset][i] + graph[i][to]
    edges.insert(0, index + 1)
    if len(depth[0]) != len(edges):
        backward(depth, edges, numeric_subset ^ (1 << index), index, graph)
    else:
        return

def construct(binary):
    r = []
    for i in range(len(binary)):
        if binary[i] == '1':
            r.append(i)
    return r

def read():
    n, m = map(int, input().split())
    graph = [[Max_t] * n for _ in range(n)]
    for _ in range(m):
        u, v, weight = map(int, input().split())
        u -= 1
        v -= 1
        graph[u][v] = graph[v][u] = weight
    return graph

if __name__ == '__main__':
    sol(*opt(read()))
