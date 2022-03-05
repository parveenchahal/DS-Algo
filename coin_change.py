# https://leetcode.com/problems/coin-change/

# Method 1 (Bottom-Up)
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        MAX = 0x7fffffffffffffff
        dp = [MAX] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[amount] if dp[amount] != MAX else -1


# Method 2 (Top-Down)
class Solution:
    
    MAX = 0x7fffffffffffffffffffff
    
    def _coin_change(self, i, n, coins, amount, memo):
        if i >= n or amount < 0:
            return self.MAX
        if amount == 0:
            return 0
        mk = (i, amount)
        if mk in memo:
            return memo[mk]
        
        r1 = self._coin_change(i, n, coins, amount - coins[i], memo) + 1
        r2 = self._coin_change(i + 1, n, coins, amount, memo)
        memo[mk] = min(r1, r2)
        return memo[mk]
    
    def coinChange(self, coins: List[int], amount: int) -> int:
        res = self._coin_change(0, len(coins), coins, amount, {})
        return res if res != self.MAX else -1
        
