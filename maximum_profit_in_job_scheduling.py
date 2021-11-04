# https://leetcode.com/problems/maximum-profit-in-job-scheduling/


# Method 2 (Using Top-To-Down)
class Solution:
    
    def _find_next(self, i, jobs):
        _, cur_end, _ = jobs[i]
        left = i + 1
        right = len(jobs) - 1
        res = len(jobs)
        while left <= right:
            mid = left + (right - left) // 2
            if cur_end <= jobs[mid][0]:
                res = mid
                right = mid - 1
            else:
                left = mid + 1
        return res
    
    def _jobScheduling(self, i, jobs, memo):
        if i >= len(jobs):
            return 0
        if memo[i] is not None:
            return memo[i]
        next = self._find_next(i, jobs)
        r1 = jobs[i][2] + self._jobScheduling(next, jobs, memo)
        r2 = self._jobScheduling(i + 1, jobs, memo)
        r = max(r1, r2)
        memo[i] = r
        return r
    
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        jobs = [(st, ed, p) for st,ed,p in zip(startTime, endTime, profit)]
        jobs.sort()
        memo = [None] * n
        return self._jobScheduling(0, jobs, memo)
