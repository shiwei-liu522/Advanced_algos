# python3
import sys
import threading

def Post(i, graph, viewed, post):
    global clock
    viewed[i] = True
    for v in graph[i]:
        if not viewed[v]:
            Post(v, graph, viewed, post)
    post[i] = clock
    clock += 1

def FindSCCs(n, rev_graph, graph):
    global clock
    post_vertex = DFS(n, rev_graph)
    visited = [False] * (2 * n + 1)
    S = []
    S_num = [0] * (2 * n + 1)
    u = 1
    for i in post_vertex:
        if not visited[i]:
            SCC = []
            View(i, graph, visited, SCC, S_num, u)
            S.append(SCC)
            u += 1
    return S, S_num

def View(i, graph, visited, SCC, S_num, u):
    visited[i] = True
    SCC.append(i)
    S_num[i] = u
    for v in graph[i]:
        if not visited[v]:
            View(v, graph, visited, SCC, S_num, u)

def DFS(n, graph):
    global clock
    visited = [False] * (2 * n + 1)
    post = [0] * (2 * n + 1)
    for v in range(1, 2 * n + 1):
        if not visited[v]:
            Post(v, graph, visited, post)
    post = list(enumerate(post[1:], start=1))
    post.sort(key=lambda x: x[1], reverse=True)
    post_vertex = []
    for v, order in post:
        post_vertex.append(v)
    return post_vertex


def SAT(n, rev_graph, graph):
    SCCs, SCC_number = FindSCCs(n, rev_graph, graph)
    # print(SCCs, SCC_number)
    for i in range(1, n + 1):
        if SCC_number[i] == SCC_number[i + n]:
            return False
    solution = [[] for _ in range(2 * n + 1)]
    assigned = [False] * (2 * n + 1)
    for SCC in SCCs:
        for v in SCC:
            if not assigned[v]:
                assigned[v] = True
                solution[v] = 1
                if v > n:
                    solution[v - n] = 0
                    assigned[v - n] = True
                else:
                    solution[v + n] = 0
                    assigned[v + n] = True
    return solution


clock = 1
def main():
    n, m = map(int, input().split())
    edges = [[] for _ in range(2 * n + 1)]
    rev_edges = [[] for _ in range(2 * n + 1)]
    for _ in range(m):
        a, b = map(int, input().split())
        if a > 0 and b > 0:
            edges[a + n].append(b)
            edges[b + n].append(a)
            rev_edges[b].append(a + n)
            rev_edges[a].append(b + n)
        elif a < 0 and b < 0:
            edges[-a].append(-b + n)
            edges[-b].append(-a + n)
            rev_edges[-b + n].append(-a)
            rev_edges[-a + n].append(-b)
        elif a < 0 and b > 0:
            edges[-a].append(b)
            edges[b + n].append(-a + n)
            rev_edges[b].append(-a)
            rev_edges[-a + n].append(b + n)
        elif a > 0 and b < 0:
            edges[a + n].append(-b + n)
            edges[-b].append(a)
            rev_edges[-b + n].append(a + n)
            rev_edges[a].append(-b)

    result = SAT(n, rev_edges, edges)
    if not result:
        print('UNSATISFIABLE')
    else:
        print('SATISFIABLE')
        for i in range(1, n + 1):
            if result[i] > 0:
                print(i, end=' ')
            else:
                print(-i, end=' ')


sys.setrecursionlimit(10 ** 7)
threading.stack_size(2 ** 25)
threading.Thread(target=main).start()
