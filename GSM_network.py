# python3

#Problem: Assign Frequencies to the Cells of a GSM Network
#Problem Introduction:
# This problem is about assigning frequencies to the transmitting towers of the cells in a GSM network to a problem of proper coloring a graph into 3 colors.
# Then you will design and implement an algorithm to reduce this problem to an instance of SAT.
import itertools
k, q = map(int, input().split())
edges = [list(map(int, input().split())) for i in range(q)]

collection=[]
def var(vertex,color):
    return (vertex-1)*3+color

def different_color():
    for edge in edges:
        for k in range(1,4):
            collection.append([-var(edge[0],k),-var(edge[1],k),0])

def vertex_color():
    for vertex in range(1, k + 1):
        collection.append([var(vertex, k) for k in range(1, 4)] + [0])

def One_T(variables):
    collection.append(variables+[0])
    for var1, var2 in itertools.combinations(variables,2):
        collection.append([-var1,-var2,0])

def printFormula():
    vertex_color()
    different_color()
    print(len(collection),' ', k * 3)
    for i in collection:
        for var in i:
            print(var,end=" ")
        print('')

printFormula()