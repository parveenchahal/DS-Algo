# https://leetcode.com/problems/n-queens/


class Solution:
    
    def _is_valid(self, board, i, j, n):
        for k in range(n):
            if k != i and board[k][j] == 'Q':
                return False
            if k != j and board[i][k] == 'Q':
                return False
        x, y = i - 1, j - 1
        while x >= 0 and y >= 0:
            if board[x][y] == 'Q':
                return False
            x -= 1
            y -= 1
        x, y = i + 1, j + 1
        while x < n and y < n:
            if board[x][y] == 'Q':
                return False
            x += 1
            y += 1
        x, y = i - 1, j + 1
        while x >= 0 and y < n:
            if board[x][y] == 'Q':
                return False
            x -= 1
            y += 1
        x, y = i + 1, j - 1
        while x < n and y >= 0:
            if board[x][y] == 'Q':
                return False
            x += 1
            y -= 1
        return True
    
    def _solve_n_queen(self, board, n, i, res):
        if i >= n:
            t = []
            for x in board:
                t.append(''.join(x))
            res.append(t)
            return
        for j in range(n):
            if self._is_valid(board, i, j, n):
                board[i][j] = 'Q'
                self._solve_n_queen(board, n, i + 1, res)
                board[i][j] = '.'
    
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [['.'] * n for _ in range(n)]
        self._solve_n_queen(board, n, 0, res)
        return res
