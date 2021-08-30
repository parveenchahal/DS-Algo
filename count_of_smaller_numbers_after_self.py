class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums = [[nums[i], i] for i in range(n)]
        res = [0] * n
        self._invertion_count(0, n - 1, nums, res)
        return res
    
    
    def _invertion_count(self, left, right, nums, res):
        if left >= right:
            return
        mid = left + (right - left) // 2
        self._invertion_count(left, mid, nums, res)
        self._invertion_count(mid + 1, right, nums, res)
        self._merge(left, mid, right, nums, res)
    
    
    def _merge(self, left, mid, right, nums, res):
        i = left
        n1 = mid
        j = mid + 1
        n2 = right
        k = 0
        temp = [None] * (right - left + 1)
        
        while i <= n1 and j <= n2:
            if nums[i][0] <= nums[j][0]:
                res[nums[i][1]] += j - mid - 1
                temp[k] = nums[i]
                k += 1
                i += 1
            else:
                temp[k] = nums[j]
                k += 1
                j += 1
        
        while i <= n1:
            temp[k] = nums[i]
            res[nums[i][1]] += j - mid - 1
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
