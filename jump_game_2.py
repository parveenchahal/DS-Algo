# https://leetcode.com/problems/jump-game-ii/
# https://www.interviewbit.com/problems/min-jumps-array/

# Method 1 (Without using extra space)
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        max_reach = 0
        cur_jump = 0
        for i in range(n - 1):
            max_reach = max(max_reach, nums[i] + i)
            if i == cur_jump:
                res += 1
                cur_jump = max_reach
        return res


# Method 2 (Using extra space)
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)

        steps = [-1] * n
        steps[0] = 0

        if nums[0] == 0:
            if n > 1:
                return -1
            else:
                return 0

        i = 0
        j = 1
        while j < n and i < j:
            max_jump = i + nums[i]
            if j <= max_jump:
                steps[j] = steps[i] + 1
                j += 1
            else:
                i += 1
        return steps[n - 1]


r = Solution().jump([1,6,1,1,1,1,1,1,1,1])
assert r == 4

r = Solution().jump([1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9])
assert r == 3
