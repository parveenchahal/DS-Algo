# https://leetcode.com/problems/merge-intervals/

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        intervals.sort()
        result = []
        cur = intervals[0]
        i = 1
        while i < n:
            if intervals[i][0] <= cur[1]:
                cur[1] = max(cur[1], intervals[i][1])
                i += 1
                continue
            result.append(cur)
            cur = intervals[i]
            i += 1
        result.append(cur)
        return result
