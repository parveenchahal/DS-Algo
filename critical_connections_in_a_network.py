# https://leetcode.com/problems/critical-connections-in-a-network/

class Solution:
    def _dfs(self, g, u, par, visited, cur_rank, dis_rank, low_rank, res):
        if u in visited:
            return low_rank[u]
        visited.add(u)
        cur_rank += 1
        dis_rank[u] = low_rank[u] = cur_rank
        children = 0
        for v in g[u]:
            if v == par:
                continue
            if v not in visited:
                children += 1
            v_low = self._dfs(g, v, u, visited, cur_rank, dis_rank, low_rank, res)
            
            # This part if different then usual "Find Articulation Algo"
            if v_low > dis_rank[u]:
                res.add((u, v))
            low_rank[u] = min(low_rank[u], v_low, dis_rank[v])
        return low_rank[u]
    
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        g = defaultdict(set)
        for con in connections:
            u, v = con
            g[u].add(v)
            g[v].add(u)
        res = set()
        dis_rank = {}
        low_rank = {}
        self._dfs(g, 0, None, set(), 0, dis_rank, low_rank, res)
        return res
