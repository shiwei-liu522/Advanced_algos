#Python3

import sys
import threading

class Vertex:
    def __init__(self, weight):
        self.children = []
        self.weight = weight

def Read():
    size = int(input())
    tree = [Vertex(weight) for weight in map(int, input().split())]
    for i in range(1, size):
        a, b = list(map(int, input().split()))
        tree[a - 1].children.append(b - 1)
        tree[b - 1].children.append(a - 1)
    return tree

def MaxWeight(tree):
    size = len(tree)
    if size == 0:
        return 0
    Depth = [-1] * size
    depth = DFS(tree, 0, -1, Depth)
    return depth

def DFS(tree, vertex, parent, Depth):
    if -1 == Depth[vertex]:
        if 1 == len(tree[vertex].children) and 0 != vertex:
            Depth[vertex] = tree[vertex].weight
        else:
            m1 = tree[vertex].weight
            for u in tree[vertex].children:
                if u != parent:
                    for w in tree[u].children:
                        if w != vertex:
                            m1 += DFS(tree, w, u, Depth)
            m0 = 0
            for u in tree[vertex].children:
                if u != parent:
                    m0 += DFS(tree, u, vertex, Depth)
            Depth[vertex] = max(m1, m0)
    return Depth[vertex]

sys.setrecursionlimit(10**6)
threading.stack_size(2**26)

def main():
    tree = Read()
    weight = MaxWeight(tree)
    print(weight)
threading.Thread(target=main).start()