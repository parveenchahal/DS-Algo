# https://leetcode.com/problems/minimum-window-substring/

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        m = {}
        if s == t:
            return s
        
        if n < len(t):
            return ''
        
        for x in t:
            try:
                m[x] += 1
            except KeyError:
                m[x] = 1
                
        j = 0
        i = 0
        MAX = 'Random' * (n + 1)
        res = MAX
        tc = len(t)
        while i < n:
            try:
                m[s[i]] -= 1
                if m[s[i]] >= 0: tc -= 1
            except:
                pass
            i += 1
            if tc > 0:
                continue
                
            while j < i:
                try:
                    if m[s[j]] < 0:
                        m[s[j]] += 1
                        j += 1
                    else:
                        break
                except:
                    j += 1
            if i - j < len(res):
                res = s[j:i]
        return res if res != MAX else ''
