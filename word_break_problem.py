# https://leetcode.com/problems/word-break/

# Method 1 (DP)
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        d = set(wordDict)
        dp = [False] * (n + 1)
        dp[0] = True
        
        for size in range(1, n + 1):
            for i in range(size):
                if dp[i] and s[i:size] in d:
                    dp[size] = True
                    break
        return dp[n]


# Method 2 (DP)
class Solution:
    def wordBreak(self, st: str, wordDict: List[str]) -> bool:
        n = len(st)
        d = set(wordDict)
        dp = [[False] * n for _ in range(n)]
        
        for s in range(1, n + 1):
            for i in range(n - s + 1):
                j = i + s - 1
                x = st[i:j + 1]
                if x in d:
                    dp[i][j] = True
                else:
                    for p in range(i, j):
                        if dp[i][p] and dp[p + 1][j]:
                            dp[i][j] = True
                            break
        return dp[0][n - 1]
