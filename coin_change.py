# https://leetcode.com/problems/coin-change/

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        m = amount + 1
        MAX = amount + 1
        dp = [MAX] * m
        dp[0] = 0
        for i in range(n):
            for j in range(coins[i], m):
                dp[j] = min(dp[j], dp[j - coins[i]] + 1)
        return dp[amount] if dp[amount] < MAX else -1
