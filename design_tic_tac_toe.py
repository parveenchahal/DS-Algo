# https://leetcode.com/problems/design-tic-tac-toe/

# Method 1
class TicTacToe:
    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.n = n
        self.row_map = [defaultdict(lambda: 0) for _ in range(n)]
        self.col_map = [defaultdict(lambda: 0) for _ in range(n)]
        self.left_diag = defaultdict(lambda: 0)
        self.right_diag = defaultdict(lambda: 0)
        self.mat = [[None] * n for _ in range(n)]

    def is_valid(self, row, col):
        n = self.n
        if row < 0 or row >= n or col < 0 or col >= n:
            return False
        if self.mat[row][col] is not None:
            return False
        return True
        
    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        n = self.n
        if not self.is_valid(row, col):
            return 0
        self.mat[row][col] = player
        self.row_map[row][player] += 1
        self.col_map[col][player] += 1
        if row == col:
            self.left_diag[player] += 1
        if row == n - 1 - col:
            self.right_diag[player] += 1
        
        return player if (self.row_map[row][player] >= n \
            or self.col_map[col][player] >= n \
            or self.left_diag[player] >= n \
            or self.right_diag[player] >= n) else 0

    
# Method 2
class TicTacToe:
    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.n = n
        self.mat = [[None] * n for _ in range(n)]
        self.row_count = [0] * n
        self.col_count = [0] * n
        self.left_diag_count = 0
        self.right_diag_count = 0
        
    def is_valid(self, row, col):
        n = self.n
        if row < 0 or row >= n or col < 0 or col >= n:
            return False
        if self.mat[row][col] is not None:
            return False
        return True
        
    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        n = self.n
        if not self.is_valid(row, col):
            return 0
        player = 1 if player == 1 else -1
        self.mat[row][col] = player
        self.row_count[row] += player
        self.col_count[col] += player
        if row == col:
            self.left_diag_count += player
        if row == n - 1 - col:
            self.right_diag_count += player
        if abs(self.row_count[row]) == n \
            or abs(self.col_count[col]) == n \
            or abs(self.left_diag_count) == n \
            or abs(self.right_diag_count) == n:
            return 1 if player == 1 else 2
        return 0
