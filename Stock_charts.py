#Python3
graphs = []

class Charts:
    def read(self):
        a, b = map(int, input().split())
        data = [list(map(int, input().split())) for i in range(a)]
        return data

    def is_smaller(self, stock, i, data):
        result = True
        if data[i][0] == data[stock][0]:
            return False

        for j in range(len(data[i])):
            if data[i][j] <= data[stock][j]:
                return False
        return True

    def construct(self, data, a):
        graph = [[]] * (2 * a + 2)
        for i in range(2 * a + 2):
            if i == 0:
                graph[i] = [(0, 0)] + [(1, 0)] * (a) + [(0, 0)] * (
                            a + 1)
            else:
                graph[i] = [(0, 0)] * (2 * a + 2)
        for i in range(len(data)):
            graph[i + a + 1][2*a + 1] = (1, 0)
            for j in range(len(data)):
                if i != j:
                    if self.is_smaller(i, j, data):
                        graph[i + 1][a + j + 1] = (1, 0)

        return graph

    def DepthFirst(self, graph, a):
        viewed = []
        stack = [(-1, 0)]
        list_edge_in_augmenting_path = []
        parent = {0: -1}
        while stack != []:
            id_e, vertex = stack.pop(0)
            viewed.append(vertex)
            for key, edge in enumerate(graph[vertex]):
                capacity, flow = edge
                if capacity - flow > 0 and key not in viewed:
                    stack.insert(0, (vertex, key))
                    parent[key] = vertex
                    if key == 2 * a + 1:
                        child = key
                        while (parent[child] != -1):
                            list_edge_in_augmenting_path.insert(0, (parent[child], child))
                            child = parent[child]
                        return list_edge_in_augmenting_path
        return -1



    def Breadth_First(self, graph, a):
        queue = [(0, -1)]
        viewed = []
        list_edge = []
        parent = {0: -1}
        while queue != []:
            vertex, id_e = queue.pop(0)
            viewed.append(vertex)
            for key, edge in enumerate(graph[vertex]):
                capacity, flow = edge
                if capacity - flow > 0 and key not in viewed:
                    queue.append((key, vertex))
                    parent[key] = vertex
                    if key == 2 * +1:
                        child = key
                        while (parent[child] != -1):
                            list_edge.insert(0, (parent[child], child))
                            child = parent[child]
                        return (list_edge)
        return -1



    def add(self, graph, list_edge):
        for value in list_edge:
            i, j = value
            graph[i][j] = (graph[i][j][0], graph[i][j][1] + 1)
            graph[j][i] = (graph[j][i][0], graph[j][i][1] - 1)

    def min_charts(self, data):
        flow = 0
        n = len(data)
        graph = self.construct(data, n)
        list_edge_in_augmenting_path = []
        while True:
            list_edge_in_augmenting_path = self.DepthFirst(graph, n)
            if list_edge_in_augmenting_path == -1:
                break
            else:
                self.add(graph, list_edge_in_augmenting_path)
                flow += 1
        return n - flow

    def write(self, result):
        print(result)

    def solve(self):
        data = self.read()
        result = self.min_charts(data)
        self.write(result)


if __name__ == '__main__':
    stock_charts = Charts()
    stock_charts.solve()