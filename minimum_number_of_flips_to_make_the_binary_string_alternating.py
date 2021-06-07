# https://leetcode.com/problems/minimum-number-of-flips-to-make-the-binary-string-alternating/

import math

class Solution:
    def minFlips(self, s: str) -> int:
        window_size = len(s)

        # Space complexity is O(N), this solution can be converted to O(1) space complexity.
        # Instead of actual rotation just change the "front" and "rear" pointers in array.
        s = s * 2
        n = len(s)
        as1 = "01" * (n // 2)
        as2 = "10" * (n // 2)

        count = math.inf
        count1 = 0
        count2 = 0

        for i in range(n):
            if as1[i] != s[i]: count1 += 1
            if as2[i] != s[i]: count2 += 1

            if i < window_size:
                continue

            if as1[i - window_size] != s[i - window_size]: count1 -= 1
            if as2[i - window_size] != s[i - window_size]: count2 -= 1

            count = min(count, min(count1, count2))
        return count

r = Solution().minFlips('01001001101')
assert r == 2