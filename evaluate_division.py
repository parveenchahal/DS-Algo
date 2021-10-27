# https://leetcode.com/problems/evaluate-division/


class Solution:
    
    def _dfs(self, u, val, expr, target, visited):
        if u == target:
            return val
        if u in visited:
            return -1
        visited.add(u)
        res = -1
        for v in expr[u]:
            res = self._dfs(v, val * expr[u][v], expr, target, visited)
            if res != -1:
                return res
        visited.discard(u)
        return res
    
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        expr = defaultdict(dict)
        
        for exp,val in zip(equations, values):
            a, b = exp
            expr[a][b] = val
            expr[b][a] = 1 / val
        res = []
        for q in queries:
            a, b = q
            visited = set([a])
            r = -1
            for x in expr[a]:
                r = self._dfs(x, expr[a][x], expr, b, visited)
                if r != -1:
                    break
            res.append(r if r != -1 else -1.0)
        return res
