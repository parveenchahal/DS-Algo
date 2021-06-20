# https://leetcode.com/problems/unique-paths/

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        mat = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(m):
            mat[0][i] = 1
        for i in range(n):
            mat[i][0] = 1

        for i in range(1, n):
            for j in range(1, m):
                mat[i][j] = mat[i - 1][j] + mat[i][j - 1]
        return mat[n - 1][m - 1]
