from disjoint_set import DisjointSet
from graph import Edge

#
# https://www.hackerrank.com/challenges/kruskalmstrsub/problem
#

def kruskals(edges, total_nodes):
    edges = sorted(edges, key=lambda x: x.wt)

    ds = DisjointSet()
    for i in range(1, total_nodes + 1):
        ds.add_set(i)
    
    s = 0
    for edge in edges:
        if ds.find(edge.u) != ds.find(edge.v):
            s += edge.wt
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