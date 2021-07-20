# https://leetcode.com/problems/permutations/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        def backtrack(first, n, result):
            if first == n:
                result.append(nums[:])
            
            for i in range(first, n):
                # swapping
                nums[first], nums[i] = nums[i], nums[first]
                
                backtrack(first + 1, n, result)
                
                # reverting the swap
                nums[first], nums[i] = nums[i], nums[first]
        result = []
        backtrack(0, n, result)
        return result
