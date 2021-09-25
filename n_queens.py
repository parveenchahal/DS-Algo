# https://leetcode.com/problems/n-queens/

# Method 1

class Solution:
    
    def _is_valid(self, i, j, n, rows_set, cols_set, diag_set, anti_diag_set):
        return i not in rows_set \
            and j not in cols_set \
            and (i + j) not in diag_set \
            and (n - 1 - (j - i)) not in anti_diag_set
    
    def _solve_n_queen(self, board, n, i, rows_set, cols_set, diag_set, anti_diag_set, res):
        if i >= n:
            t = []
            for x in board:
                t.append(''.join(x))
            res.append(t)
            return
        for j in range(n):
            if self._is_valid(i, j, n, rows_set, cols_set, diag_set, anti_diag_set):
                board[i][j] = 'Q'
                rows_set.add(i)
                cols_set.add(j)
                d = i + j
                diag_set.add(d)
                ad = n - 1 - (j - i)
                anti_diag_set.add(ad)
                self._solve_n_queen(board, n, i + 1, rows_set, cols_set, diag_set, anti_diag_set, res)
                rows_set.discard(i)
                cols_set.discard(j)
                diag_set.discard(d)
                anti_diag_set.discard(ad)
                board[i][j] = '.'
    
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [['.'] * n for _ in range(n)]
        rows_set = set()
        cols_set = set()
        diag_set = set()
        anti_diag_set = set()
        self._solve_n_queen(board, n, 0, rows_set, cols_set, diag_set, anti_diag_set, res)
        return res


# Method 2

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
