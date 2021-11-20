# https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/


class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0
        
        nums.sort()
        res = float('inf')
        
        # First three
        res = min(res, nums[-1] - max(nums[:4]))
        
        # Last three
        res = min(res, min(nums[-4:]) - nums[0])
        
        # First one and Last two
        res = min(res, min(nums[-3:]) - max(nums[:2]))
        
        # First two and Last one
        res = min(res, min(nums[-2:]) - max(nums[:3]))
        
        return res
        
        
