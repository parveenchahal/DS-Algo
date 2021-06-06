# https://leetcode.com/problems/queries-on-number-of-points-inside-a-circle/

from typing import List
import math

class Solution:
    def _compute_lookup(self, points):

        # Max coordinate distance 
        n = int(math.sqrt(501 ** 2 + 501 ** 2))
        self._lookup = [[] for _ in range(n)]
        for x in points:
            index = int(math.sqrt(x[0] ** 2 + x[1] ** 2))
            self._lookup[index].append(x)
        
    def _two_point_distance(self, x, y):
        return math.sqrt((y[0] - x[0]) ** 2 + (y[1] - x[1]) ** 2)
    
    def _count_for_a_circle(self, c):
        lookup = self._lookup
        cc = [c[0], c[1]]
        r = c[2]
        d = self._two_point_distance([0,0], cc)
        min_dist = max(0, int(math.floor(d - r)))
        max_dist = min(len(lookup) - 1, int(math.ceil(d + r)))
        count = 0
        for i in range(min_dist, max_dist + 1):
            for x in lookup[i]:
                if self._two_point_distance(cc, x) <= r:
                    count += 1
        return count
    
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        self._compute_lookup(points)
        result = []
        for c in queries:
            result.append(self._count_for_a_circle(c))
        return result
