# https://leetcode.com/problems/shortest-bridge/

class Solution:
    
    dirs = [[0, 1], [0, -1], [-1, 0], [1, 0]]
    
    def _dfs(grid, u, R, C, name):
        ui, uj = u
        if grid[ui][uj] == 0 or grid[ui][uj] == name:
            return
        grid[ui][uj] = name
        for dir in Solution.dirs:
            vi, vj = ui + dir[0], uj + dir[1]
            if vi < 0 or vi >= R or vj < 0 or vj >= C:
                continue
            Solution._dfs(grid, (vi, vj), R, C, name)
                
    def _bfs(grid, u, name1, name2, R, C):
        h = [(0, u[0], u[1])]
        visited = [[False] * C for _ in range(R)]
        while len(h) > 0:
            ud, ui, uj = heapq.heappop(h)
            for dir in Solution.dirs:
                vi, vj = ui + dir[0], uj + dir[1]
                if vi < 0 or vi >= R or vj < 0 or vj >= C or visited[vi][vj]:
                    continue
                visited[vi][vj] = True
                vd = ud
                if grid[vi][vj] == name2:
                    return vd
                if grid[vi][vj] != name1:
                    vd += 1
                heapq.heappush(h, (vd, vi, vj))
        return -1
        
    def shortestBridge(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len(grid[0])
        islands = []
        name = 2
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 1:
                    Solution._dfs(grid, (i, j), R, C, name)
                    islands.append((i, j))
                    name += 1
        return Solution._bfs(grid, islands[0], 2, 3, R, C)
