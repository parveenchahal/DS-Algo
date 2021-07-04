# https://leetcode.com/problems/repeated-substring-pattern/

# Method 1


# Method 2 (Using LPS(KMP))
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        lps = [0] * n
        j = 0
        i = 1
        while i < n:
            if s[j] == s[i]:
                lps[i] = j + 1
                i += 1
                j += 1
                continue
            elif j <= 0:
                lps[i] = 0
                i += 1
            else:
                j = lps[j - 1]
        print(lps)
        l = lps[-1]
        if l == 0:
            return False
        d = n - l
        return n % d == 0
