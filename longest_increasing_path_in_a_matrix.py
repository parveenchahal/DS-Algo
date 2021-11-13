# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/


class Solution:
    
    DIRS = ((-1, 0), (1, 0), (0, -1), (0, 1))
    
    def _dfs(self, u, matrix, R, C, visited, memo):
        ui, uj = u
        if u in visited:
            return 0
        if memo[ui][uj] is not None:
            return memo[ui][uj]
        visited.add(u)
        memo[ui][uj] = 1
        for dir in self.DIRS:
            vi, vj = ui + dir[0], uj + dir[1]
            if vi < 0 or vi >= R or vj < 0 or vj >= C or matrix[ui][uj] >= matrix[vi][vj]:
                continue
            v = (vi, vj)
            d = self._dfs(v, matrix, R, C, visited, memo)
            if memo[ui][uj] is not None:
                memo[ui][uj] = max(memo[ui][uj], d + 1)
        visited.discard(u)
        return memo[ui][uj]
    
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        R = len(matrix)
        C = len(matrix[0])
        memo = [[None] * C for _ in range(R)]
        for i in range(R):
            for j in range(C):
                self._dfs((i, j), matrix, R, C, set(), memo)
        res = 1
        for row in memo:
            res = max(res, max(row))
        return res
