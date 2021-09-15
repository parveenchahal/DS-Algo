# https://leetcode.com/problems/minimum-degree-of-a-connected-trio-in-a-graph/


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
