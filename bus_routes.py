# https://leetcode.com/problems/bus-routes/


class Solution:
    
    def _bfs(self, g, starts, targets):
        q = deque([(x, 1) for x in starts])
        visited = set(starts)
        MAX = 0x7fffffffffffffffffff
        res = MAX
        while len(q) > 0:
            u, d = q.popleft()
            if u in targets:
                res = min(res, d)
            for v in g[u]:
                if v not in visited:
                    visited.add(v)
                    q.append((v, d + 1))
        return res if res != MAX else -1
    
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        n = len(routes)
        routes = list(map(set, routes))
        g = defaultdict(set)
        starts = []
        targets = []
        for i, r1 in enumerate(routes):
            if source in r1:
                starts.append(i)
            if target in r1:
                targets.append(i)
            for j in range(i+1, n):
                r2 = routes[j]
                if len(set.intersection(r1, r2)) > 0:
                    g[i].add(j)
                    g[j].add(i)
        return self._bfs(g, starts, targets)
