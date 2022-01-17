class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def size(self):
        return len(self.adjacency_list)

    def get_nodes(self):
        return list(self.adjacency_list.keys())

    def add_node(self, value):
        vertex = Vertex(value)
        self.adjacency_list[vertex] = []
        return vertex

    def add_edge(self, start_vtx, end_vtx, weight = 0):
        """
    Adds a directional edge"""

        if not end_vtx in self.adjacency_list:
            raise KeyError

        edge = Edge(end_vtx, weight)
        self.adjacency_list[start_vtx].append(edge)

    def get_neighbors(self, vertex):
        return self.adjacency_list[vertex]

class Edge:
    def __init__(self, vertex, weight=0):
        self.vertex = vertex
        self.weight = weight


class Vertex:
    def __init__(self, value):
        self.value = value
