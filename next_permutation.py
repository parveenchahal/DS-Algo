# https://leetcode.com/problems/next-permutation/

class Solution:
    def _find_drop_from_right(self, nums):
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                return i
        return -1
    
    def _reverse(self, nums, i, j):
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
            
    def _find_just_greater_num_index(self, nums, x):
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] > x:
                return i
        
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)
        if n <= 0:
            return
        drop_index = self._find_drop_from_right(nums)
        if drop_index < 0:
            self._reverse(nums, 0, n - 1)
            return
        just_greater_index = self._find_just_greater_num_index(nums, nums[drop_index])
        nums[just_greater_index], nums[drop_index] = nums[drop_index], nums[just_greater_index]
        self._reverse(nums, drop_index + 1, n - 1)
