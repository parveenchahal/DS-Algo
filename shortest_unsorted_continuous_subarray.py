# https://leetcode.com/problems/shortest-unsorted-continuous-subarray/

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        
        left = -1
        right = -1
        
        max_so_far = nums[0]
        for i in range(1, n):
            if nums[i] < max_so_far:
                right = i
            max_so_far = max(max_so_far, nums[i])
            
        if right == -1:
            return 0
        
        min_so_far = nums[n - 1]
        for i in range(n - 1, -1, -1):
            if nums[i] > min_so_far:
                left = i
            min_so_far = min(min_so_far, nums[i])
        
        return right - left + 1
