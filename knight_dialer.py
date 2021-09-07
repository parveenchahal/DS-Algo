# https://leetcode.com/problems/knight-dialer/

class Solution:
    MOD = 10 ** 9 + 7
    valid_moves = [[4,6], [6,8], [7,9], [4,8], [3,9,0], [], [1,7,0], [2,6], [1,3], [2,4]]
    
    def _get_next(self, prev_count):
        cur_count = [0] * 10
        for i in range(10):
            for m in self.valid_moves[i]:
                cur_count[i] += prev_count[m]
                cur_count[i] %= self.MOD
        return cur_count
    
    def knightDialer(self, n: int) -> int:
        res = [1] * 10
        for s in range(2, n + 1):
            res = self._get_next(res)
        total = 0
        for x in res:
            total += x
            total %= self.MOD
        return total
