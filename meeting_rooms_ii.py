# https://leetcode.com/problems/meeting-rooms-ii/

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        ins = [x[0] for x in intervals]
        outs = [x[1] for x in intervals]
        ins.sort()
        outs.sort()
        i = 0
        j = 0
        res = 0
        count = 0
        while i < n and j < n:
            if ins[i] < outs[j]:
                count += 1
                i += 1
            else:
                count -= 1
                j += 1
            res = max(res, count)
        return res
