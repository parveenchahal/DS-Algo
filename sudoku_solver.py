# https://leetcode.com/problems/sudoku-solver/


# Method 1

class Solution:
    
    def _is_valid_placement(self, i, j, rows, cols, boxes, num):
        if num in rows[i] or num in cols[j] or num in boxes[i // 3][j // 3]:
            return False
        return True
    
    def _solve_sudoku(self, i, j, board, rows, cols, boxes, changable):
        if self.found or i == 9:
            return
        if not changable[i][j]:
            if i == 8 and j == 8:
                self.found = True
            self._solve_sudoku(i + 1 if j == 8 else i, (j + 1) % 9, board, rows, cols, boxes, changable)
        else:
            for v in range(1, 10):
                x = str(v)
                if not self.found and self._is_valid_placement(i, j, rows, cols, boxes, x):
                    board[i][j] = x
                    if i == 8 and j == 8:
                        self.found = True
                    rows[i].add(x)
                    cols[j].add(x)
                    boxes[i // 3][j // 3].add(x)
                    self._solve_sudoku(i + 1 if j == 8 else i, (j + 1) % 9, board, rows, cols, boxes, changable)
                    rows[i].discard(x)
                    cols[j].discard(x)
                    boxes[i // 3][j // 3].discard(x)
        
        
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.found = False
        boxes = [[set() for _ in range(3)] for _ in range(3)]
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        changable = [[True] * 9 for _ in range(9)]
        for i,row in enumerate(board):
            for j,x in enumerate(row):
                if x != '.':
                    changable[i][j] = False
        
        for i,row in enumerate(board):
            for j,x in enumerate(row):
                if x == '.':
                    continue
                bi, bj = i // 3, j // 3
                boxes[bi][bj].add(x)
                rows[i].add(x)
                cols[j].add(x)
        self._solve_sudoku(0, 0, board, rows, cols, boxes, changable)



# Method 2
class Solution:
    
    def _is_valid_placement(self, board, boxes, i, j, num):
        #print(f'{i}, {j}')
        for k in range(9):
            if board[i][k] == num:
                return False
            if board[k][j] == num:
                return False
        if num in boxes[i // 3][j // 3]:
            return False
        return True
    
    def _solve_sudoku(self, i, j, board, boxes):
        if self.found or i == 9:
            return
        if board[i][j] != '.':
            if i == 8 and j == 8:
                self.found = True
                self.res = copy.deepcopy(board)
            self.solve(i + 1 if j == 8 else i, (j + 1) % 9, board, boxes)
        else:
            for v in range(1, 10):
                x = str(v)
                if not self.found and self.is_valid_placement(board, boxes, i, j, x):
                    board[i][j] = x
                    if i == 8 and j == 8:
                        self.found = True
                        self.res = copy.deepcopy(board)
                    boxes[i // 3][j // 3].add(x)
                    self.solve(i + 1 if j == 8 else i, (j + 1) % 9, board, boxes)
                    boxes[i // 3][j // 3].discard(x)
                    board[i][j] = '.'
    
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.found = False
        boxes = [[set() for _ in range(3)] for _ in range(3)]
        for i,row in enumerate(board):
            for j,x in enumerate(row):
                if x == '.':
                    continue
                bi, bj = i // 3, j // 3
                boxes[bi][bj].add(x)
        self.solve(0, 0, board, boxes)
        for i, row in enumerate(self.res):
            for j, x in enumerate(row):
                board[i][j] = x
        
