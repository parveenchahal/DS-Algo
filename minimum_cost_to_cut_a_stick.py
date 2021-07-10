# https://leetcode.com/problems/minimum-cost-to-cut-a-stick/

class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.sort()
        t = [0]
        t.extend(cuts)
        t.append(n)
        cuts = t
        k = len(cuts)
        
        dp = [[0] * k for _ in range(k)]
        
        for s in range(3, k + 1):
            for i in range(k - s + 1):
                j = i + s - 1
                dp[i][j] = 0x7fffffffffffffffff
                for t in range(i + 1, j):
                    dp[i][j] = min(dp[i][j], (cuts[j] - cuts[i]) + dp[i][t] + dp[t][j])
        return dp[0][k - 1]
