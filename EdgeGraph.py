class EdgeGraph:
    def __init__(self, nodes=1):
        self.__count_of_nodes = nodes - 1
        self.__edges = 0
        self.__edge_dict = {}

    def add_node(self, count=1):
        self.__count_of_nodes += count

    def add_edge(self, head, tail):
        self.__edge_dict[self.__edges] = (head, tail)
        self.__edges += 1

    def remove_edge(self, edge):
        del self.__edges[edge]

    @property
    def nodes(self):
        return self.__count_of_nodes

    @property
    def edges(self):
        return self.__edge_dict

    @property
    def edge_list(self):
        return [item for _, item in self.__edge_dict.items()]

    def __str__(self):
        return f'Graph(\n\t#Nodes: {self.__count_of_nodes + 1},\t#Edges: {self.__edges}\n)'
