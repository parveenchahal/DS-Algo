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
        
        # Need to store degree separatly
        # because we'll be keep on dicarding sets
        degree = {}
        for x in g:
            degree[x] = len(g[x])
        res = self.MAX
        for u,v in edges:
            for common_conn in g[u].intersection(g[v]):
                trio_degree = degree[u] + degree[v] + degree[common_conn] - 6
                if trio_degree >= 0:
                    res = min(res, trio_degree)
                # Discard u and v from common_conn
                # That has been considered already.
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
