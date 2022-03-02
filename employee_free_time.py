# https://leetcode.com/problems/employee-free-time/

# Method 1 (Number of intervals are small in number, this method run faster)
"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        Interval.__repr__ = lambda self: str((self.start, self.end))
        intervals = [interval for emp_intervals in schedule for interval in emp_intervals]
        intervals.sort(key=lambda x: (x.start, x.end))
        
        res = []
        end = intervals[0].end
        for interval in intervals:
            a, b = interval.start, interval.end
            if end < a:
                res.append(Interval(end, a))
            end = max(b, end)
        return res



# Method 2 (If there are large number of employees and large number of intervals per employee then this method works faster)
"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""
class Solution:
    
    def _merge_two_sorted_lists(self, l1, l2):
        n1 = len(l1)
        n2 = len(l2)
        i = 0
        j = 0
        res = []
        while i < n1 and j < n2:
            if l1[i].start <= l2[j].start:
                res.append(l1[i])
                i += 1
            else:
                res.append(l2[j])
                j += 1
        while i < n1:
            res.append(l1[i])
            i += 1
        while j < n2:
            res.append(l2[j])
            j += 1
        return res
    
    def _merge_k_sorted_lists(self, q):
        q = deque(q)
        if len(q) == 0:
            raise ValueError('Empty Queue')
        
        while len(q) > 1:
            a = q.popleft()
            b = q.popleft()
            c = self._merge_two_sorted_lists(a, b)
            q.append(c)
        
        return q[0]
        
    def _merge_intervals(self, intervals):
        n = len(intervals)
        res = [intervals[0]]
        for i in range(n):
            interval = intervals[i]
            st, ed = interval.start, interval.end
            if st >= res[-1].start and st <= res[-1].end:
                res[-1].end = max(res[-1].end, ed)
            else:
                res.append(interval)
        return res
    
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        intervals = self._merge_k_sorted_lists(schedule)
        merged_intervals = self._merge_intervals(intervals)
        res = []
        for i in range(1, len(merged_intervals)):
            res.append(Interval(merged_intervals[i - 1].end, merged_intervals[i].start))
        return res



# Method 2
"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""
class Solution:
    
    def _merge_two_sorted_lists(self, l1, l2):
        n1 = len(l1)
        n2 = len(l2)
        i = 0
        j = 0
        res = []
        while i < n1 and j < n2:
            if l1[i] <= l2[j]:
                res.append(l1[i])
                i += 1
            else:
                res.append(l2[j])
                j += 1
        while i < n1:
            res.append(l1[i])
            i += 1
        while j < n2:
            res.append(l2[j])
            j += 1
        return res
    
    
    def _merge_k_sorted_lists(self, q):
        if len(q) == 0:
            raise ValueError('Empty Queue')
        
        while len(q) > 1:
            a = q.popleft()
            b = q.popleft()
            c = self._merge_two_sorted_lists(a, b)
            q.append(c)
        
        return q[0]
    
    
    def _separate_ins_outs_in_sorted(self, schedule):
        ins_q = deque()
        outs_q = deque()
        for sc in schedule:
            ins_q.append([x.start for x in sc])
            outs_q.append([x.end for x in sc])
        return self._merge_k_sorted_lists(ins_q), self._merge_k_sorted_lists(outs_q)
    
    
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        ins, outs = self._separate_ins_outs_in_sorted(schedule)
        n = len(ins)
        i = j = 0
        cur_time = 0
        count = 0
        res = []
        while i < n and j < n:
            if ins[i] <= outs[j]:
                count += 1
                if len(res) > 0 and len(res[-1]) == 1:
                    res[-1].append(ins[i])
                i += 1
            else:
                count -= 1
                if count == 0:
                    res.append([outs[j]])
                j += 1
        return list(map(lambda x: Interval(x[0], x[1]), res))
