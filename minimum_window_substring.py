# https://leetcode.com/problems/minimum-window-substring/

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        m = {}
        if s == t:
            return s
        
        if n < len(t):
            return ''
        
        m = collections.Counter(t)
        
        j = 0
        i = 0
        MAX = '#' * (n + 1)
        res = MAX
        tc = len(t)
        while i < n:
            try:
                m[s[i]] -= 1
                if m[s[i]] >= 0:
                    tc -= 1
            except KeyError:
                pass
            
            i += 1
            if tc > 0:
                continue
                
            while j < i:
                try:
                    if m[s[j]] >= 0:
                        break
                    m[s[j]] += 1
                except KeyError:
                    pass
                j += 1
            
            if i - j < len(res):
                res = s[j:i]
            
        return res if res != MAX else ''
