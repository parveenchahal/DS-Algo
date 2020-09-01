from typing import List

class Edge():
    def __init__(self, u, v, wt):
        self.u = u
        self.v = v
        self.wt = wt

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return self.__str__()

class Graph():

    is_directed_graph: bool
    _map: dict

    def __init__(self, directed_graph=False):
        self.is_directed_graph = directed_graph
        self._map = {}

    def add(self, edge: Edge):
        if not isinstance(edge, Edge):
            raise TypeError('edge is expected as type of Edge')
        for i in range(2):
            try:
                self._map[edge.u].append(edge)
                break
            except KeyError:
                self._map[edge.u] = []
        if not self.is_directed_graph:
            for i in range(2):
                try:
                    self._map[edge.v].append(Edge(edge.v, edge.u, edge.wt))
                    break
                except KeyError:
                    self._map[edge.v] = []

    def children(self, u) -> List[Edge]:
        try:
            return self._map[u]
        except KeyError:
            return None

    def get_all_edges(self):
        return [x for l in self._map for x in self._map[l]]

    def __str__(self):
        return str(self._map)

    def __repr__(self):
        return self.__str__()

