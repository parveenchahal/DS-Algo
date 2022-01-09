# https://leetcode.com/problems/majority-element/

# Method 1 (Boyer-Moore Majority Voting Algorithm)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = None
        count = 0
        for x in nums:
            if count == 0:
                majority = x
            
            if x == majority:
                count += 1
            else:
                count -= 1
        return majority

# Method 2 (Sorting)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]
