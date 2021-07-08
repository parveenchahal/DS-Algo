# https://leetcode.com/problems/contiguous-array/

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        nums = list(map(lambda x: x if x == 1 else -1, nums))
        for i in range(1, n):
            nums[i] += nums[i -1]
        res = 0
        m = {0: -1}
        for i in range(n):
            try:
                res = max(res, i - m[nums[i]])
            except KeyError:
                m[nums[i]] = i
        return res
