# https://leetcode.com/problems/count-all-valid-pickup-and-delivery-options/


class Solution:
    
    MOD = 10 ** 9 + 7
    
    def _ap_sum(self, n):
        return (n * (1 + n)) // 2
    
    def countOrders(self, n: int) -> int:
        dp = [0, 1]
        for i in range(2, n + 1):
            dp.append((dp[i - 1] * self._ap_sum(2 * i - 1)) % self.MOD)
        return dp[-1]
