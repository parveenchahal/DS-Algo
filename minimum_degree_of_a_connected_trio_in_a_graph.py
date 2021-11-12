# https://leetcode.com/problems/minimum-degree-of-a-connected-trio-in-a-graph/


# Method 1
class Solution:
    MAX = 0x7ffffffffffff
    
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        g = defaultdict(set)
        for edge in edges:
            u, v = edge
            g[u].add(v)
            g[v].add(u)
        degree = {}
        for x in g:
            degree[x] = len(g[x])
        res = self.MAX
        for u in range(1, n + 1):
            for v in g[u]:
                intersections = g[u].intersection(g[v])
                for common_conn in intersections:
                    trio_degree = degree[u] + degree[v] + degree[common_conn] - 6
                    if trio_degree >= 0:
                        res = min(res, trio_degree)
                    g[common_conn].discard(u)
                    g[common_conn].discard(v)
        return res if res != self.MAX else -1


# Method 2
class Solution:
    MAX = 0x7ffffffffffff
    
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        g = defaultdict(set)
        for edge in edges:
            u, v = edge
            g[u].add(v)
            g[v].add(u)
        res = self.MAX
        visited = set()
        for i in range(1, n + 1):
            if i in g:
                visited.add(i)
                combi = combinations(g[i] - visited, 2)
                for a,b in combi:
                    if a in g[b]:
                        res = min(res, len(g[i]) + len(g[a]) + len(g[b]) - 6)
        return res if res != self.MAX else -1
