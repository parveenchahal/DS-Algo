# https://leetcode.com/problems/two-sum/

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        m = {}
        for i in range(n):
            x = target - nums[i]
            if x in m:
                return sorted([m[x], i])
            m[nums[i]] = i
        return []
                