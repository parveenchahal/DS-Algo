# https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = dp[i - 1] + nums[i - 1]
        
        res = -0x800000000000000
        min_so_far = dp[0]
        for i in range(1, n + 1):
            res = max(res, dp[i] - min_so_far)
            min_so_far = min(min_so_far, dp[i])
        return res
