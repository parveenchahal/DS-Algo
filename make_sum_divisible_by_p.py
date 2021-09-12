# https://leetcode.com/problems/make-sum-divisible-by-p/

from typing import List

# Method 1
class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        n = len(nums)
        s = sum(nums)
        r = s % p
        if r == 0:
            return 0
        sum_so_far = 0
        m = {0: -1}
        MAX = n
        result = MAX
        for i in range(n):
            sum_so_far += nums[i]
            sum_so_far = sum_so_far % p
            x = sum_so_far - r
            if x < 0:
                x += p
            if x in m:
                result = min(result, i - m[x])
            m[sum_so_far] = i
        return result if result != MAX else -1


# Method 2
class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        n = len(nums)
        r = sum(nums) % p
        if r == 0:
            return 0
        sum_so_far = 0
        m = {0: -1}
        MAX = n
        res = MAX
        for i, x in enumerate(nums):
            sum_so_far += x
            sum_so_far = sum_so_far % p
            m[sum_so_far] = i
            t = (sum_so_far - r) % p
            if t in m:
                res = min(res, i - m[t])
        return res if res < n else -1
