# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        st = set()
        result = 0
        i = 0
        j = 0
        while j < n:
            
            if s[j] in st:
                st.remove(s[i])
                i += 1
                continue
            result = max(result, j - i + 1)
            j += 1
        return result

assert 3 == Solution().lengthOfLongestSubstring("abcabcbb")