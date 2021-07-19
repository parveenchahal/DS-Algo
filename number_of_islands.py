# https://leetcode.com/problems/number-of-islands/


class Solution:
    def _dfs(self, grid, i, j, n, m):
        if i < 0 or i >= n or j < 0 or j >= m:
            return
        if grid[i][j] == '0':
            return
        
        grid[i][j] = '0'
        self._dfs(grid, i + 1, j, n, m)
        self._dfs(grid, i - 1, j, n, m)
        self._dfs(grid, i, j + 1, n, m)
        self._dfs(grid, i, j - 1, n, m)
    
    def numIslands(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])
        count = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    self._dfs(grid, i, j, n, m)
                    count += 1
        return count
