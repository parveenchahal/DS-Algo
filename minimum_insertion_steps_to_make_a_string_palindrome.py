# https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/

class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        
        # Calculating for 2 size
        for i in range(n - 1):
            j = i + 1
            if s[i] != s[j]:
                dp[i][j] = 1
        
        for k in range(3, n + 1):
            for i in range(n - k + 1):
                j = i + k - 1
                if s[i] != s[j]:
                    dp[i][j] = 1 + min(dp[i][j - 1], dp[i + 1][j])
                else:
                    dp[i][j] = dp[i + 1][j - 1]
        return dp[0][n - 1]
            
