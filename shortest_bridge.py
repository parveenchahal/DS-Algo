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
        visited = [[False] * C for _ in range(R)]
        
        h = [(0, u[0], u[1])]
        visited[u[0]][u[1]] = True
        while len(h) > 0:
            ud, ui, uj = heapq.heappop(h)
            for dir in Solution.dirs:
                vi, vj = ui + dir[0], uj + dir[1]
                if vi < 0 or vi >= R or vj < 0 or vj >= C or visited[vi][vj]:
                    continue
                visited[vi][vj] = True
                if grid[vi][vj] == name2:
                    return ud
                vd = 0
                if grid[vi][vj] != name1:
                    vd = ud + 1
                heapq.heappush(h, (vd, vi, vj))
        return -1
        
    def shortestBridge(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len(grid[0])
        island2 = None
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 1:
                    Solution._dfs(grid, (i, j), R, C, 2)
                    island2 = (i, j)
                    break
            if island2:
                break
        return Solution._bfs(grid, island2, 2, 1, R, C)
