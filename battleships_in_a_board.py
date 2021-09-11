# https://leetcode.com/problems/battleships-in-a-board/


class Solution:    
    def countBattleships(self, board: List[List[str]]) -> int:
        R = len(board)
        C = len(board[0])
        count = 0
        for i in range(R):
            for j in range(C):
                if board[i][j] != 'X':
                    continue
                if i == 0 and j == 0 and board[i][j] == 'X':
                    count += 1
                    continue
                elif i > 0 and board[i - 1][j] == 'X':
                    continue
                elif j > 0 and board[i][j - 1] == 'X':
                    continue
                count += 1
        return count
