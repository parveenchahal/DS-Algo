# https://leetcode.com/problems/cutting-ribbons

from typing import List

class Solution:
    
    def _count_ribbons(self, ribbons, size):
        count = 0
        for x in ribbons:
            count += x // size
        return count
    
    def _binary_search(self, ribbons, l, r, k):
        result = None
        while l <= r:
            mid = (l + r) // 2
            count = self._count_ribbons(ribbons, mid)
            if count >= k:
                result = mid
                l = mid + 1
            else:
                r = mid - 1
        return int(result)
                
    
    def maxLength(self, ribbons: List[int], k: int) -> int:
        max_len = int(sum(ribbons) // k)
        if max_len <= 0:
            return 0
        return self._binary_search(ribbons, 1, max_len, k)

r = Solution().maxLength([100000,1,100000,100000,100000,100000,100000,100000,100000,100000,100000,100000,100000,100000,100000,100000,100000,100000,100000,100000,100000,100000,100000,100000,100000,100000,100000,100000,100000,100000,100000,100000,100000,100000,100000,100000,100000,100000,100000,100000,100000,100000,100000,100000,100000,100000,100000,100000,100000,100000], 50)
assert r == 50000

r = Solution().maxLength([9,7,5], 2)
assert r == 7