# https://leetcode.com/problems/shortest-distance-from-all-buildings/


class Solution:
    
    MAX = float('inf')
    
    DIRS = ((-1, 0), (1, 0), (0, -1), (0, 1))
        
    def _bfs(self, s, grid, R, C, total_dist, total_house_visits):
        visited = [[False] * C for _ in range(R)]
        q = deque([(s[0], s[1], 0)])
        visited[s[0]][s[1]] = True
        while len(q) > 0:
            ui, uj, ud = q.popleft()
            for dir in self.DIRS:
                vi, vj, vd = ui + dir[0], uj + dir[1], ud + 1
                if vi < 0 or vi >= R or vj < 0 or vj >= C:
                    continue
                if grid[vi][vj] == 0 and not visited[vi][vj]:
                    visited[vi][vj] = True
                    total_dist[vi][vj] += vd
                    total_house_visits[vi][vj] += 1
                    q.append((vi, vj, vd))

    
    def shortestDistance(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len(grid[0])
        total_dist = [[0] * C for _ in range(R)]
        total_house_visits = [[0] * C for _ in range(R)]
        
        existing_houses_count = 0
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 1:
                    existing_houses_count += 1
                    self._bfs((i, j), grid, R, C, total_dist, total_house_visits)
        
        res = self.MAX
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 0:
                    if existing_houses_count == total_house_visits[i][j]:
                        res = min(res, total_dist[i][j])
        return res if res != self.MAX else -1
        
