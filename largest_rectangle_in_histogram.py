# https://leetcode.com/problems/largest-rectangle-in-histogram/

from typing import List

class Solution:

    def _pop_until_and_get_max_area(self, h, st, i):
        result = 0
        n = len(h)
        while len(st) > 0:
            if i < n and h[st[-1]] <= h[i]:
                break
            j = st.pop()
            width = (i - st[-1] - 1) if len(st) > 0 else i
            a = width * h[j]
            result = max(result, a)
        return result

    def largestRectangleArea(self, h: List[int]) -> int:
        n = len(h)
        st = []
        result = 0
        for i in range(n):
            if len(st) > 0 and h[st[-1]] >= h[i]:
                result = max(result, self._pop_until_and_get_max_area(h, st, i))
            st.append(i)
            
        if len(st) > 0:
            result = max(result, self._pop_until_and_get_max_area(h, st, n))
        print(result)
        return result

assert 10 == Solution().largestRectangleArea([2,1,5,6,2,3])
