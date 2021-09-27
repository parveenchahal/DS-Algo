# https://leetcode.com/problems/reverse-pairs/


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        n = len(nums)
        return self._merge_sort(0, n - 1, nums)
    
    def _merge_sort(self, left, right, nums):
        if left >= right:
            return 0
        mid = left + (right - left) // 2
        count = 0
        count += self._merge_sort(left, mid, nums)
        count += self._merge_sort(mid + 1, right, nums)
        count += self._merge(left, mid, right, nums)
        return count
    
    def _merge(self, left, mid, right, nums):
        count = 0
        j = mid + 1
        
        count = 0
        for i in range(left, mid + 1):
            while j <= right and nums[i] > (2 * nums[j]):
                j += 1
            count += j - (mid + 1)
        i = left
        n1 = mid
        j = mid + 1
        n2 = right
        k = 0
        temp = [None] * (right - left + 1)
        
        while i <= n1 and j <= n2:
            if nums[i] <= nums[j]:
                temp[k] = nums[i]
                k += 1
                i += 1
            else:
                temp[k] = nums[j]
                k += 1
                j += 1
        
        while i <= n1:
            temp[k] = nums[i]
            k += 1
            i += 1
        
        while j <= n2:            
            temp[k] = nums[j]
            k += 1
            j += 1
        
        k = left
        for t in temp:
            nums[k] = t
            k += 1
        return count
