# https://leetcode.com/problems/candy-crush/


class Solution:
    
    def _settle_down(self, board, R, C):
        for j in range(C):
            zero = R - 1
            for i in range(R - 1, -1, -1):
                if board[i][j] != 0:
                    board[i][j], board[zero][j] = board[zero][j], board[i][j]
                    zero -= 1
                    
    def _make_neg_zero(self, board, R, C):
        changed = False
        for i in range(R):
            for j in range(C):
                if board[i][j] < 0:
                    changed = True
                    board[i][j] = 0
        return changed
    
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        #for row in board: print(list(map(lambda x: ' ' * (4 - len(str(x))) + str(x), row)))
        #print("################################")
        R = len(board)
        C = len(board[0])
        changed = True
        while changed:
            for i in range(R):
                for j in range(C):
                    typ = abs(board[i][j])
                    if typ == 0:
                        continue
                    # Check down
                    count = 0
                    for k in range(i + 1, min(R, i + 3)):
                        if abs(board[k][j]) == typ:
                            count += 1
                            if count == 2:
                                break
                        else:
                            break
                    if count == 2:
                        for k in range(i, i + 3):
                            board[k][j] = -abs(board[k][j])
                    
                    # Check right
                    count = 0
                    for k in range(j + 1, min(C, j + 3)):
                        if abs(board[i][k]) == typ:
                            count += 1
                            if count == 2:
                                break
                        else:
                            break
                    if count == 2:
                        for k in range(j, j + 3):
                            board[i][k] = -abs(board[i][k])
            changed = self._make_neg_zero(board, R, C)
            self._settle_down(board, R, C)
            #for row in board: print(list(map(lambda x: ' ' * (4 - len(str(x))) + str(x), row)))
            #print("################################")
        return board
