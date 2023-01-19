#Python3
class Edge:
    def __init__(self, u, v, weight):
        self.u = u
        self.v = v
        self.weight = weight
        self.flow = 0

class FlowGraph:

    def __init__(self, n):
        self.edges = []
        self.graph = [[] for _ in range(n)]

    def size(self):
        return len(self.graph)

    def get_ids(self, start):
        return self.graph[start]

    def get_edge(self, id):
        return self.edges[id]

    def add_edge(self, start, end, weight):
        # Note that we first append a forward edge and then a backward edge,
        # so all forward edges are stored at even indices (starting from 0),
        # whereas backward edges are stored at odd indices.
        forward_edge = Edge(start, end, weight)
        backward_edge = Edge(end, start, 0)
        self.graph[start].append(len(self.edges))
        self.edges.append(forward_edge)
        self.graph[end].append(len(self.edges))
        self.edges.append(backward_edge)

    def add_flow(self, id, flow):
        # To get a backward edge for a true forward edge (i.e id is even), we should get id + 1
        # due to the described above scheme. On the other hand, when we have to get a "backward"
        # edge for a backward edge (i.e. get a forward edge for backward - id is odd), id - 1
        # should be taken.
        #
        # It turns out that id ^ 1 works for both cases. Think this through!
        self.edges[id].flow += flow
        self.edges[id ^ 1].flow -= flow


def BFS(graph,start,end):
    queue=[(start,-1)]
    viewed=[]
    list_edge_in_augmenting_path=[]
    parent={}
    while queue!=[]:
            city,id_e=queue.pop(0)
            viewed.append(city)
            for edge_id in graph.get_ids(city):
                edge=graph.get_edge(edge_id)
                if edge.u==city and edge.v!=city and edge.v not in viewed and edge.weight-edge.flow>0:
                    queue.append((edge.v,edge_id))
                    parent[edge_id]=id_e
                    if edge.v==end:
                        child=edge_id
                        list_edge_in_augmenting_path.append(child)
                        while(parent[child]!=-1):
                            list_edge_in_augmenting_path.append(parent[child])
                            child=parent[child]
                        return (viewed,list_edge_in_augmenting_path)
    return ([],[])

def max_flow(graph, start, end):
    flow = 0
    while True:
        viewed,list_edge_in_augmenting_path=BFS(graph,start,end)
        if viewed!=[]:
            min_capacity=float('inf')
            for edge in list_edge_in_augmenting_path:
                if graph.get_edge(edge).weight-graph.get_edge(edge).flow<min_capacity:
                    min_capacity= graph.get_edge(edge).weight - graph.get_edge(edge).flow
            for edge in list_edge_in_augmenting_path:
                graph.add_flow(edge,min_capacity)
            flow+=min_capacity
        else:
            break
    return flow

def read():
    vertex_count, edge_count = map(int, input().split())
    graph = FlowGraph(vertex_count)
    for _ in range(edge_count):
        u, v, capacity = map(int, input().split())
        graph.add_edge(u - 1, v - 1, capacity)
    return graph

if __name__ == '__main__':
    graph = read()
    print(max_flow(graph, 0, graph.size() - 1))