# https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/

class Solution:
    def _match_subseq(self, s, w):
        w_len = len(w)
        j = 0
        for i in range(len(s)):
            if s[i] == w[j]:
                j += 1
            if j >= w_len:
                return True
        return False
    
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        n = len(s)
        res = ''
        ml = 0
        for w in dictionary:
            if self._match_subseq(s, w):
                if len(w) > ml:
                    ml = len(w)
                    res = w
                elif len(w) == ml:
                    res = min(res, w)
        return res
