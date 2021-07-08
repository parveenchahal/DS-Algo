# https://leetcode.com/problems/sort-colors/

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        
        z = 0
        while z < n and nums[z] == 0: z += 1 
        
        t = len(nums) - 1
        while t >= 0 and nums[t] == 2: t -= 1
        
        i = z
        while i <= t:
            if nums[i] == 0 and z < i:
                nums[z], nums[i] = nums[i], nums[z]
                while z < n and nums[z] == 0: z += 1
            elif nums[i] == 2:
                nums[t], nums[i] = nums[i], nums[t]
                while t >= 0 and nums[t] == 2: t -= 1
            else:
                i += 1
