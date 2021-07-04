# https://leetcode.com/problems/3sum/

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        result = []
        for k in range(n - 2):
            if k > 0 and nums[k] == nums[k - 1]:
                continue
            i = k + 1
            j = n - 1
            while i < j:
                if i > k + 1 and nums[i] == nums[i - 1]:
                    i += 1
                    continue
                if j < n - 1 and nums[j] == nums[j + 1]:
                    j -= 1
                    continue
                x = nums[i] + nums[j]
                if x < -nums[k]:
                    i += 1
                elif x > -nums[k]:
                    j -= 1
                else:
                    result.append(sorted([nums[k], nums[i], nums[j]]))
                    i += 1
                    j -= 1
        return result
