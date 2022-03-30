class VertexGraph:
    def __init__(self, nodes=1):
        self.__nodes = nodes - 1
        self.__edges = 0
        self.__graph = {i: [] for i in range(nodes)}

    @staticmethod
    def from_edge_graph(edges_list, nodes):
        graph = VertexGraph(nodes)
        for edge in edges_list:
            graph.add_edge(*edge)

        return graph

    def add_vertex(self):
        self.__nodes += 1
        self.__graph[self.__nodes] = []

    def add_edge(self, first, second):
        self.__graph[first].append(second)
        self.__graph[second].append(first)
        self.__edges += 1

    def are_adjacent(self, first, second):
        return first in self.__graph[second]

    def show(self):
        for index, neighbors in self.__graph.items():
            print(f'{index}: {neighbors}')
