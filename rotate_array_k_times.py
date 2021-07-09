# https://leetcode.com/problems/rotate-array/

class Solution:
    def _reverse(self, nums, i, j):
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
        
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n
        
        if k <= 0:
            return
        
        self._reverse(nums, 0, n - 1)
        self._reverse(nums, 0, k - 1)
        self._reverse(nums, k, n - 1)
