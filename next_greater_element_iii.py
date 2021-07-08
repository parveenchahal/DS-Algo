# https://leetcode.com/problems/next-greater-element-iii/

class Solution:
    
    def _find_drop(self, arr):
        n = len(arr)
        i = n - 2
        while i >= 0:
            if arr[i] < arr[i + 1]:
                return i
            i -= 1
        return -1
    
    def _find_just_greater(self, arr, x):
        for i in range(len(arr) - 1, -1, -1):
            if arr[i] > x:
                return i
    
    def _reverse(self, arr, i):
        j = len(arr) - 1
        while i < j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
        
    
    def nextGreaterElement(self, n: int) -> int:
        arr = list(str(n))
        
        d = self._find_drop(arr)
        if d < 0:
            return -1
        
        g = self._find_just_greater(arr, arr[d])
        
        arr[d], arr[g] = arr[g], arr[d]
        
        self._reverse(arr, d + 1)
        
        res =  int(''.join(arr))
        
        return res if res <= 0x7fffffff else -1
