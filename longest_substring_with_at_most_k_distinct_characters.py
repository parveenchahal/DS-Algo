# https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        n = len(s)
        m = {}
        i = 0
        j = 0
        res = 0
        while j < n:
            try:
                m[s[j]] += 1
            except KeyError:
                m[s[j]] = 1
            
            while len(m) > k:
                m[s[i]] -= 1
                if m[s[i]] <= 0:
                    del m[s[i]]
                i += 1
            
            res = max(res, j - i + 1)
            j += 1
        return res
