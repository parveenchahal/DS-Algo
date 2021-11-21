# https://leetcode.com/problems/sudoku-solver/


class Solution:
    
    def _is_valid_placement(self, pos, rows, cols, boxes, num):
        i, j = pos
        if num in rows[i] or num in cols[j] or num in boxes[i // 3][j // 3]:
            return False
        return True
        
    def _next_pos(self, pos):
        i, j = pos
        return (i if j < 8 else i + 1, (j + 1) % 9)
    
    def _solve_sudoku(self, pos, board, rows, cols, boxes):
        i, j = pos
        if i >= 9:
            return True
        if board[i][j] != '.':
            next_pos = self._next_pos(pos)
            return self._solve_sudoku(next_pos, board, rows, cols, boxes)
        else:
            for c in range(1, 10):
                c = str(c)
                if self._is_valid_placement(pos, rows, cols, boxes, c):
                    board[i][j] = c
                    rows[i].add(c)
                    cols[j].add(c)
                    boxes[i // 3][j // 3].add(c)
                    next_pos = self._next_pos(pos)
                    found = self._solve_sudoku(next_pos, board, rows, cols, boxes)
                    if found:
                        return True
                    
                    rows[i].discard(c)
                    cols[j].discard(c)
                    boxes[i // 3][j // 3].discard(c)
                    board[i][j] = '.'
            return False
    
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [[set() for _ in range(3)] for _ in range(3)]
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
                    boxes[i // 3][j // 3].add(board[i][j])
        self._solve_sudoku((0, 0), board, rows, cols, boxes)
