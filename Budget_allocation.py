# python3
from sys import stdin

n, m = list(map(int, stdin.readline().split()))
F = []
for i in range(n):
    F += [list(map(int, stdin.readline().split()))]
S = list(map(int, stdin.readline().split()))

collections = []
for i, coefficient in enumerate(F):
    non_coeff = [(j, coefficient[j]) for j in range(m) if 0 != coefficient[j]]
    l = len(non_coeff)
    for x in range(2**l):
        currSet = [non_coeff[j] for j in range(l) if 1 == ((x/2**j)%2)//1]
        currSum = 0
        for coeff in currSet:
            currSum += coeff[1]
        if currSum > S[i]:
            collections.append([-(coeff[0]+1) for coeff in currSet] + [coeff[0]+1 for coeff in non_coeff if not coeff in currSet])

if 0 == len(collections):
    collections.append([1, -1])
    m = 1
print(len(collections), m)

for item in collections:
    item.append(0)
    print(' '.join(map(str, item)))