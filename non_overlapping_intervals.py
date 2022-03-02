# https://leetcode.com/problems/non-overlapping-intervals/

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        intervals.sort(key=lambda x: x[1])
        count = 0
        end = intervals[0][1]
        for i in range(1, n):
            if intervals[i][0] >= end:
                end = intervals[i][1]
            else:
                count += 1
        return count
