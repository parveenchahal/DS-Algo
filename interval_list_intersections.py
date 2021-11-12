# https://leetcode.com/problems/interval-list-intersections/


class Solution:
    
    def _intersection(self, i1, i2):
        res = max(i1[0], i2[0]), min(i1[1], i2[1])
        return res if res[0] <= res[1] else None
    
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        n1 = len(firstList)
        n2 = len(secondList)
        i = 0
        j = 0
        res = []
        while i < n1 and j < n2:
            interval1 = firstList[i]
            interval2 = secondList[j]
            intersection = self._intersection(interval1, interval2)
            if intersection is not None:
                res.append(intersection)
            if interval1[1] <= interval2[1]:
                i += 1
            else:
                j += 1
        return res
