# https://leetcode.com/problems/maximum-number-of-points-with-cost/


class Solution:
        
    def maxPoints(self, points: List[List[int]]) -> int:
        MIN = -0xffffffffffffff
        R = len(points)
        C = len(points[0])
        dp = [[0] * C for _ in range(R)]
        dp[0] = list(points[0])
        for i in range(1, R):
            ma = MIN
            for j in range(C):
                ma = max(ma, dp[i - 1][j] + j)
                dp[i][j] = ma + points[i][j] - j
            ma = MIN
            for j in range(C - 1, -1, -1):
                ma = max(ma, dp[i - 1][j] - j)
                dp[i][j] = max(dp[i][j], ma + points[i][j] + j)
        return max(dp[-1])
