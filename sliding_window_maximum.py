# https://leetcode.com/problems/sliding-window-maximum/


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        res = []
        for i,x in enumerate(nums):
            l = i - (k - 1)
            while len(dq) > 0 and nums[dq[-1]] < x:
                dq.pop()
            dq.append(i)
            while dq[0] < l:
                dq.popleft()
            if i >= k - 1:
                res.append(nums[dq[0]])
        return res
