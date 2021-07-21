# https://leetcode.com/problems/subarray-sum-equals-k/

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        sum_so_far = 0
        count = 0
        m = {0: 1}
        for i in range(n):
            sum_so_far += nums[i]
            x = sum_so_far - k
            try:
                count += m[x]
            except KeyError:
                pass
            
            try:
                m[sum_so_far] += 1
            except KeyError:
                m[sum_so_far] = 1
        return count
