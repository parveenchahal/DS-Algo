# https://leetcode.com/problems/container-with-most-water/

from typing import List

class Solution:
    def maxArea(self, h: List[int]) -> int:
        n = len(h)
        i = 0
        j = n - 1
        result = min(h[i], h[j]) * (j - i)
        while i < j:
            if h[i] < h[j]:
                i += 1
            else:
                j -= 1
            result = max(result, min(h[i], h[j]) * (j - i))
        return result

assert 62 == Solution().maxArea([6,4,3,1,4,6,99,62,1,2,6])

