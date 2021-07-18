# https://leetcode.com/problems/subarray-sum-equals-k/

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        sum_so_far = [0] * (n + 1)
        for i in range(1, n + 1):
            sum_so_far[i] = sum_so_far[i - 1] + nums[i - 1]
        
        count = 0
        m = {0: 1}
        for i in range(1, n + 1):
            x = sum_so_far[i] - k
            try:
                count += m[x]
            except KeyError:
                pass
            
            try:
                m[sum_so_far[i]] += 1
            except KeyError:
                m[sum_so_far[i]] = 1
        return count
