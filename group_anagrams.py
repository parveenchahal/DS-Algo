# https://leetcode.com/problems/group-anagrams/

class Solution:
    def _find_counts(self, s):
        counts = [0] * 26
        b = ord('a')
        for x in s:
            counts[ord(x) - b] += 1
        return tuple(counts)
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = {}
        for x in strs:
            cts = self._find_counts(x)
            try:
                m[cts].append(x)
            except KeyError:
                m[cts] = [x]
        return m.values()
