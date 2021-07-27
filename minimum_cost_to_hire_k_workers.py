# https://leetcode.com/problems/minimum-cost-to-hire-k-workers/


class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        n = len(quality)
        ratio = [(wage[i] / quality[i], i) for i in range(n)]
        ratio.sort()

        MAX = 0x7fffffffffffffffffff
        res = MAX

        h = [-quality[ratio[i][1]] for i in range(k - 1)]
        heapq.heapify(h)

        q_sum = -sum(h)
        
        for i in range(k - 1, n):
            r, index = ratio[i]
            res = min(res, q_sum * r + wage[index])
            heapq.heappush(h, -quality[index])
            q_sum += quality[index]
            q_sum += heapq.heappop(h)
        return res
