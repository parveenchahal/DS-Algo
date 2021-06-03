# https://leetcode.com/problems/jump-game-vii/

class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        if  n <= 0 or s[0] == 1:
            return False
        dp = [False] * n
        dp[0] = True
        for j in range(minJump, maxJump + 1):
            if s[j] == '0':
                dp[j] = True
        zero_count = 0
        bucket_min = 0
        bucket_max = maxJump - minJump
        for i in range(bucket_min, bucket_max + 1):
            if dp[i]:
                zero_count += 1
        for j in range(maxJump + 1, n):
            bucket_max += 1
            if dp[bucket_max]:
                zero_count += 1
            if dp[bucket_min]:
                zero_count -= 1
                zero_count = max(0, zero_count)
            bucket_min += 1
            if s[j] == '0' and zero_count > 0:
                dp[j] = True
        return dp[n - 1]

r = Solution().canReach("011010", 2, 3)
assert r == True