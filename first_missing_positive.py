# https://leetcode.com/problems/first-missing-positive/


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums) + 1
        nums.append(-1)
        i = 0
        while i < n:
            if nums[i] is None:
                i += 1
                continue
            j = nums[i]
            if j == i:
                i += 1
            elif j >= n or j <= 0 or nums[j] == j:
                nums[i] = None
                i += 1
            else:
                nums[i], nums[j] = nums[j], nums[i]
        for i in range(1, n):
            if nums[i] is None:
                return i
        return n
