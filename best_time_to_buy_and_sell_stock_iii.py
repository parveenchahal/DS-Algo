# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        min_so_far = prices[0]
        t1 = [0] * n
        for i in range(1, n):
            t1[i] = max(t1[i - 1], prices[i] - min_so_far)
            min_so_far = min(min_so_far, prices[i])
        res = t1[-1]
        max_so_far = prices[-1]
        for i in range(n - 2, 0, -1):
            res = max(res, t1[i - 1] + max_so_far - prices[i])
            max_so_far = max(max_so_far, prices[i])
        return res
