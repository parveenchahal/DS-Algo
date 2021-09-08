# https://leetcode.com/problems/regular-expression-matching/

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        ns = len(s)
        np = len(p)
        dp = [[False] * (ns + 1) for _ in range(np + 1)]
        
        dp[0][0] = True
        for i in range(1, np + 1):
            dp[i][0] = p[i - 1] == '*' and dp[i - 2][0]
        
        for i in range(1, np + 1):
            for j in range(1, ns + 1):
                if p[i - 1] == '*':
                    dp[i][j] = dp[i - 2][j] \
                        or dp[i - 1][j] \
                        or (i > 1\
                            and (p[i - 2] == '.' or p[i - 2] == s[j - 1]) \
                            and (dp[i - 1][j - 1] or dp[i][j - 1])\
                        )
                elif p[i - 1] == '.':
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = dp[i - 1][j - 1] and s[j - 1] == p[i - 1]
        return dp[np][ns]
