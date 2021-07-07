# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        res = 0
        for i in range(1, n):
            x = prices[i] - prices[i - 1]
            if x > 0:
                res += x
        return res
