# https://leetcode.com/problems/palindromic-substrings/

# Solution 1
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        
        count = 0
        for k in range(n):
            i, j = k, k
            while i >=0 and j < n:
                if s[i] != s[j]:
                    break
                count += 1
                i -= 1
                j += 1
                
        for k in range(n - 1):
            i, j = k, k + 1
            while i >=0 and j < n:
                if s[i] != s[j]:
                    break
                count += 1
                i -= 1
                j += 1
        return count

# Solution 2
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False]*n for _ in range(n)]
        
        count = 0
        for i in range(0, n):
            dp[i][i] = True
            count += 1

        for size in range(2, n + 1):
            for i in range(0, n - size + 1):
                l = i
                r = i + size - 1
                if s[l] == s[r]:
                    _l = l + 1
                    _r = r - 1
                    if(_l > _r or dp[_l][_r]):
                        dp[l][r] = True
                        count += 1
        return count
