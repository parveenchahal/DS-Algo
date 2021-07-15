# https://leetcode.com/problems/decode-ways/

# Method 1 (Constant space)
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if s[0] == '0':
            return 0
        
        one_back = 1
        two_back = 1
        
        for i in range(1, n):
            t = 0
            if s[i] !='0':
                t = one_back
            
            x = int(s[i - 1: i + 1])
            if x >= 10 and x <= 26:
                t += two_back
            
            one_back, two_back = t, one_back
        
        return one_back


# Method 2 (DP: Extra space)
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * n
        if s[0] != '0':
            dp[0] = 1
        if n == 1:
            return dp[0]
        if s[1] != '0':
            dp[1] = dp[0]
        x = int(s[:2])
        if x >= 10 and x <= 26:
            dp[1] += 1
        for i in range(2, n):
            if s[i] !='0':
                dp[i] = dp[i - 1]
            x = int(s[i - 1: i + 1])
            if x >= 10 and x <= 26:
                dp[i] += dp[i - 2]
        return dp[n - 1]
      
