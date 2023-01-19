# python3
import itertools
n, m = map(int, input().split())
edge = [ list(map(int, input().split())) for i in range(m) ]

collections = []
positions = range(1, n+1)
adj = [[] for _ in range(n)]
for i, j in edge:
    adj[i-1].append(j-1)
    adj[j-1].append(i-1)

def var_number(i, j):
    return n*i + j

def One_T(lit):
    collections.append([t for t in lit])
    for pair in itertools.combinations(lit, 2):
        collections.append([-t for t in pair])

for j in positions:
    One_T([var_number(i, j) for i in range(n)])

for i in range(n):
    One_T([var_number(i, j) for j in positions])

for j in positions[:-1]:
    for i, nodes in enumerate(adj):
        collections.append([-var_number(i, j)] + [var_number(n, j+1) for n in nodes])

print(len(collections), n*n)
for item in collections:
    item.append(0)
    print(' '.join(map(str, item)))