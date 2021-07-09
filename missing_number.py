# https://leetcode.com/problems/missing-number/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        ap_sum = n * (1 + n) // 2
        return ap_sum - sum(nums)
