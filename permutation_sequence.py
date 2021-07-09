# https://leetcode.com/problems/permutation-sequence/

class Solution:
    def _get_permutation(self, n, k, fixed, nums):
        if n <= 0:
            return ''
        
        bucket_size = self.factorial[n - 1]
        for x in nums:
            if x in fixed:
                continue
            
            if k - bucket_size > 0:
                k -= bucket_size
                continue
            
            fixed.add(x)
            return str(x) + self._get_permutation(n - 1, k, fixed, nums)
    
    
    def getPermutation(self, n: int, k: int) -> str:
        # pre computing factorial
        self.factorial = [1]
        for i in range(1, n + 1):
            self.factorial.append(self.factorial[i - 1] * i)
        
        return self._get_permutation(n, k, set(), [i for i in range(1, n + 1)])
