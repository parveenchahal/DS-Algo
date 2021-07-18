# https://leetcode.com/problems/one-edit-distance/

class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if s == t:
            return False
        
        ns = len(s)
        nt = len(t)
        if ns < nt:
            # maintaining s as biggest
            s, t = t, s
            ns, nt = nt, ns
        
        i = 0
        j = 0
        while i < ns and j < nt and s[i] == t[j]:
            i += 1
            j += 1
            
        x = i
        
        i = ns - 1
        j = nt - 1
        while i >= 0 and j >= 0 and s[i] == t[j]:
            i -= 1
            j -= 1
        
        y = i
        
        if x == ns - 1 and y == 0:
            # s = aaaa
            # t = aaa
            return True
        
        return x == y
