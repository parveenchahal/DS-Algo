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


# Optimized memory
class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        n = len(quality)
        sorted_ratio_indices = list(range(n))
        sorted_ratio_indices.sort(key=lambda i: wage[i] / quality[i])

        MAX = 0x7fffffffffffffffffff
        res = MAX

        h = [-quality[sorted_ratio_indices[i]] for i in range(k - 1)]
        heapq.heapify(h)

        quality_sum = -sum(h)
        
        for i in range(k - 1, n):
            index = sorted_ratio_indices[i]
            ratio = wage[index] / quality[index]
            quality_sum += quality[index]
            res = min(res, quality_sum * ratio)
            heapq.heappush(h, -quality[index])
            quality_sum += heapq.heappop(h)
        return res
