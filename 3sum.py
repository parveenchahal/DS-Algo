# https://leetcode.com/problems/3sum/

# Method 1 (Without sorting)
class Solution:
    def twoSum(self, nums, i, j, target) -> List[int]:
        s = set()
        res = []
        for k in range(i, j + 1):
            x = target - nums[k]
            if x in s:
                res.append([x, nums[k]])
            s.add(nums[k])
        return res
    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = set()
        for k in range(n - 2):
            t = self.twoSum(nums, k + 1, n - 1, -nums[k])
            for x in t:
                x.append(nums[k])
                x.sort()
                result.add(tuple(x))
        return result

# Method 2 (Sorting)
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
                
                # have fixed two numbers to need to check for 3rd
                if i > k + 1 and nums[i] == nums[i - 1]:
                    i += 1
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
