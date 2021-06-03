# https://leetcode.com/problems/minimum-speed-to-arrive-on-time/

from typing import List
import math

MAX = 10000000

class Solution:
    def _time_taken(self, dist, speed):
        n = len(dist)
        t = 0
        for i in range(n - 1):
            t += math.ceil(dist[i] / speed)
        t += (dist[-1] / speed)
        return t
        
    def _binary_search(self, dist, hour, i, j):
        while i < j:
            mid = (i + j) // 2
            t = self._time_taken(dist, mid)
            if t > hour:
                i = mid + 1
            elif t < hour:
                j = mid - 1
            else:
                return mid
        if self._time_taken(dist, i) > hour:
            return i + 1 if i + 1 <= MAX else -1
        return i if i <= MAX else -1
    
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        min_speed = max(int(sum(dist) // hour), 1)
        max_speed = MAX
        if hour <= len(dist) - 1:
            return -1
        return self._binary_search(dist, hour, min_speed, max_speed)

r = Solution().minSpeedOnTime([2,1,5,4,4,3,2,9,2,10], 75.12)
assert r == 1

r = Solution().minSpeedOnTime([69], 4.6)
assert r == 15

r = Solution().minSpeedOnTime([1,1,100000], 2.01)
assert r == 10000000

r = Solution().minSpeedOnTime([1,3,2], 2.7)
assert r == 3

r = Solution().minSpeedOnTime([1,3,1,2], 6)
assert r == 2