# https://leetcode.com/problems/edit-distance

class Solution:
    MAX = 0x7fffffffffffff
    
    def minDistance(self, word1: str, word2: str) -> int:
        n1 = len(word1)
        n2 = len(word2)
        
        dp = [[self.MAX] * (n1 + 1) for _ in range(n2 + 1)]
        for i in range(n1 + 1):
            dp[0][i] = i
        for i in range(n2 + 1):
            dp[i][0] = i
        
        for i in range(1, n2 + 1):
            for j in range(1, n1 + 1):
                if word2[i - 1] != word1[j - 1]:
                    dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1]) + 1
                else:
                    dp[i][j] = dp[i - 1][j - 1]
        return dp[n2][n1]
