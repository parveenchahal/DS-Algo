# https://leetcode.com/problems/sort-colors/

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        zero = 0
        cur = 0
        two = n - 1
        while zero <= two and nums[zero] == 0:
            zero += 1
            cur += 1
        while two >= zero and nums[two] == 2:
            two -= 1
        while cur <= two:
            if nums[cur] == 0:
                nums[cur], nums[zero] = nums[zero], nums[cur]
                zero += 1
                cur = max(cur, zero)
            elif nums[cur] == 2:
                nums[cur], nums[two] = nums[two], nums[cur]
                two -= 1
            else:
                cur += 1
