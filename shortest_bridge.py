# https://leetcode.com/problems/shortest-bridge/

class Solution:
    
    dirs = [[0, 1], [0, -1], [-1, 0], [1, 0]]
    
    def _is_bounary(grid, x, R, C):
        for dir in Solution.dirs:
            vi, vj = x[0] + dir[0], x[1] + dir[1]
            if vi >= 0 and vi < R and vj >= 0 and vj < C:
                if grid[vi][vj] == 0:
                    return True
        return False
    
    def _populate_boundary(grid, u, boundary, R, C, name):
        ui, uj = u
        if grid[ui][uj] in [0, name]:
            return
        grid[ui][uj] = name
        if Solution._is_bounary(grid, u, R, C):
            boundary.append(u)
        for dir in Solution.dirs:
            vi, vj = ui + dir[0], uj + dir[1]
            if vi >= 0 and vi < R and vj >= 0 and vj < C:
                Solution._populate_boundary(grid,[vi, vj], boundary, R, C, name)
                
    def _bfs(grid, boundaries, name1, name2, R, C):
        visited = [[False] * C for _ in range(R)]
        q = deque()
        for x in boundaries:
            q.append((0, x[0], x[1]))
            visited[x[0]][x[1]] = True
        while len(q) > 0:
            ud, ui, uj = q.popleft()
            for dir in Solution.dirs:
                vi, vj = ui + dir[0], uj + dir[1]
                if vi < 0 or vi >= R or vj < 0 or vj >= C or visited[vi][vj]:
                    continue
                if grid[vi][vj] == name2:
                    return ud
                visited[vi][vj] = True
                vd = ud + 1 if grid[vi][vj] != name1 else 0
                q.append((vd, vi, vj))
        return -1
        
    def shortestBridge(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len(grid[0])
        island2 = None
        boundaries = []
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 1:
                    Solution._populate_boundary(grid, (i, j), boundaries, R, C, 2)
                    island2 = (i, j)
                    break
            if island2:
                break
        return Solution._bfs(grid, boundaries, 2, 1, R, C)
