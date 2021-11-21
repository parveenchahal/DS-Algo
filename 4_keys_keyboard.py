# https://leetcode.com/problems/4-keys-keyboard/


class Solution:
    def maxA(self, n: int) -> int:
        dp = [0, 1, 2, 3, 4, 5]
        for i in range(6, n + 1):
            dp.append(i)
            dp[i] = max(dp[i], dp[i - 1] + 1)
            for j in range(0, 3):
                x = dp[i - 3 - j] * (j + 2)
                dp[i] = max(dp[i], x)
            
        return dp[n]
