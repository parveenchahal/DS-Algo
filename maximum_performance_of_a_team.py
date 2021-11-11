# https://leetcode.com/problems/maximum-performance-of-a-team/


class Solution:
    
    MOD = 10 ** 9 + 7
    
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        emp = list(zip(efficiency, speed))
        emp.sort(reverse=True)
        h = []
        speed_sum = 0
        perf = 0
        for cur_eff,cur_speed in emp:
            speed_sum += cur_speed
            perf = max(perf, speed_sum * cur_eff)
            heapq.heappush(h, cur_speed)
            if len(h) >= k:
                speed_sum -= heapq.heappop(h)
        return perf % self.MOD
