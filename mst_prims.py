from collections import deque
import heapq
from graph import Graph, Edge

#
# https://www.hackerrank.com/challenges/primsmstsub/problem
#

def prims(edges, total_nodes, start):
    g = Graph()
    for edge in edges:
        g.add(edge)

    heap = []
    setattr(Edge, '__lt__', lambda self, o: self.wt - o.wt < 0)

    for e in g.children(start):
        heap.append(e)
    heapq.heapify(heap)

    visited = set()
    visited.add(start)

    s = 0
    while len(heap) > 0:
        x = heapq.heappop(heap)
        if x.v in visited:
            continue
        s += x.wt
        for e in g.children(x.v):
            heapq.heappush(heap, e)
        visited.add(x.v)
    return s


if __name__ == '__main__':
    
    total_nodes, total_edges = map(int, input().rstrip().split())
    
    edges = [None] * total_edges
    for i in range(total_edges):
        u, v, w = map(int, input().rstrip().split())
        edges[i] = Edge(u, v, w)

    start = int(input())

    res = prims(edges, total_nodes, start)
    print(res)
