# https://leetcode.com/problems/jump-game/

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        max_reach = 0
        for i in range(n):
            max_reach = max(max_reach, nums[i] + i)
            if max_reach <= i:
                break
        return max_reach >= n - 1
