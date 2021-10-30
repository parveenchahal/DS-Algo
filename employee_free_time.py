# https://leetcode.com/problems/employee-free-time/


"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        ins = []
        outs = []
        for sc in schedule:
            for x in sc:
                ins.append(x.start)
                outs.append(x.end)
        ins.sort()
        outs.sort()
        n = len(ins)
        i = j = 0
        cur_time = 0
        pre_time = 0
        count = 0
        res = []
        while i < n and j < n:
            if ins[i] <= outs[j]:
                pre_time, cur_time = cur_time, ins[i]
                i += 1
                count += 1
            else:
                pre_time, cur_time = cur_time, outs[j]
                j += 1
                count -= 1
            if count == 0:
                res.append([cur_time])
            elif len(res) > 0 and len(res[-1]) == 1:
                res[-1].append(cur_time)
        return list(map(lambda x: Interval(x[0], x[1]), res))
