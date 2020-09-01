import sys
import heapq
from graph import Edge, Graph

#
# https://www.hackerrank.com/challenges/dijkstrashortreach/problem
#

class Node():
    def __init__(self, vertex, cost):
        self.vertex = vertex
        self.cost = cost

def dijkstra(edges, total_nodes, start):
    
    Node.__lt__ = lambda self, o: self.cost - o.cost < 0

    g = Graph()
    for e in edges:
        g.add(e)

    visited = set()

    heap = []
    heap.append(Node(start, 0))

    dist_map = {}

    while len(heap) > 0:
        x = heapq.heappop(heap)

        try:
            dist_map[x.vertex] = min(x.cost, dist_map[x.vertex])
        except KeyError:
            dist_map[x.vertex] = x.cost

        if x.vertex in visited:
            continue

        visited.add(x.vertex)

        for c in g.children(x.vertex):
            cur_cost = x.cost + c.wt
            if cur_cost < dist_map.get(c.v, sys.maxsize):
                heapq.heappush(heap, Node(c.v, cur_cost))

    result = []
    for i in range(1, total_nodes + 1):
        if i != start:
            result.append(dist_map.get(i, -1))
    return result

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        total_nodes, total_edges = map(int, input().rstrip().split())
        
        edges = [None] * total_edges
        for i in range(total_edges):
            u, v, w = map(int, input().rstrip().split())
            edges[i] = Edge(u, v, w)

        start = int(input())

        res = dijkstra(edges, total_nodes, start)
        print(' '.join(map(str, res)))