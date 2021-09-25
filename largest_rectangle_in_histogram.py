# https://leetcode.com/problems/largest-rectangle-in-histogram/

from typing import List

# Method 1
class Solution:

    def _find_just_smaller_indices(self, heights):
        n = len(heights)
        left_res = []
        st = [-1]
        for i,h in enumerate(heights):
            while len(st) > 1 and heights[st[-1]] >= h:
                st.pop()
            left_res.append(st[-1])
            st.append(i)
        
        right_res = []
        st = [n]
        for i,h in reversed(list(enumerate(heights))):
            while len(st) > 1 and heights[st[-1]] >= h:
                st.pop()
            right_res.append(st[-1])
            st.append(i)
        right_res.reverse()
        return left_res, right_res

    def largestRectangleArea(self, heights: List[int]) -> int:
        left_just_smaller, right_just_smaller = self._find_just_smaller_indices(heights)
        res = 0
        for i,h in enumerate(heights):
            area = h * (right_just_smaller[i] - left_just_smaller[i] - 1)
            res = max(res, area)
        return res


# Method 2
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
        return result
