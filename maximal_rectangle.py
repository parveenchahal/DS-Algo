# https://leetcode.com/problems/maximal-rectangle/


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
    
    def _largest_rectangle_area(self, heights) -> int:
        left_just_smaller, right_just_smaller = self._find_just_smaller_indices(heights)
        res = 0
        for i,h in enumerate(heights):
            area = h * (right_just_smaller[i] - left_just_smaller[i] - 1)
            res = max(res, area)
        return res
    
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        n = len(matrix)
        if n == 0:
            return 0
        m = len(matrix[0])
        if m == 0:
            return 0
        
        for i,row in enumerate(matrix):
            for j,x in enumerate(row):
                matrix[i][j] = int(x)
        
        max_area = self._largest_rectangle_area(matrix[0])
        for i in range(1, n):
            row = matrix[i]
            for j in range(m):
                if matrix[i][j] == 1:
                    matrix[i][j] += matrix[i - 1][j]
            max_area = max(max_area, self._largest_rectangle_area(row))
        return max_area
