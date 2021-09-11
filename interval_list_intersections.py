# https://leetcode.com/problems/interval-list-intersections/


class Solution:
    
    def _intersection(x, y):
        return [max(x[0], y[0]), min(x[1], y[1])]
    
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        n1 = len(firstList)
        n2 = len(secondList)
        i = j = 0
        res = []
        while i < n1 and j < n2:
            x = firstList[i]
            y = secondList[j]
            t = Solution._intersection(x, y)
            if t[0] <= t[1]:
                res.append(t)
            if x[1] <= y[1]:
                i += 1
            else:
                j += 1
        return res
