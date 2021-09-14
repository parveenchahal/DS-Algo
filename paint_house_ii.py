# https://leetcode.com/problems/paint-house-ii/


class Solution:
    def _get_min_cost(self, costs, exclude):
        n = len(costs)
        min_cost = 0x7fffff
        for i in range(n):
            if i != exclude:
                min_cost = min(min_cost, costs[i])
        return min_cost
    
    def minCostII(self, costs: List[List[int]]) -> int:
        n = len(costs)
        k = len(costs[0])
        one_back = list(costs[0])
        for i in range(1, n):
            cur = [None] * k
            for j in range(k):
                cur[j] = costs[i][j] + self._get_min_cost(one_back, j)
            one_back = cur
        return min(one_back)
