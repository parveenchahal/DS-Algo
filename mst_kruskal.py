from disjoint_set import DisjointSet

class Edge():
    u: int
    v: int
    w: int

    def __init__(self, u, v, w):
        self.u = u
        self.v = v
        self.w = w
    
    def __repr__(self):
        return str(self.__dict__)

def kruskals(edges, total_nodes):
    edges = sorted(edges, key=lambda x: x.w)

    ds = DisjointSet()
    for i in range(1, total_nodes + 1):
        ds.add_set(i)
    
    s = 0
    for edge in edges:
        if ds.find(edge.u) != ds.find(edge.v):
            s += edge.w
            ds.union(edge.u, edge.v)

    return s

if __name__ == '__main__':

    total_nodes, total_edges = map(int, input().rstrip().split())

    edges = [None] * total_edges

    for i in range(total_edges):
        u, v, w = map(int, input().rstrip().split())
        edges[i] = Edge(u, v, w)

    res = kruskals(edges, total_nodes)

    print(res)