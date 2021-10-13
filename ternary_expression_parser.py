# https://leetcode.com/problems/ternary-expression-parser/

class Solution:
    
    def parseTernary(self, exp: str) -> str:
        n = len(exp)
        st = []
        i = 0
        while len(st) > 1 or i < n:
            if len(st) > 1 and st[-2] == ':' and (i >= n or exp[i] != '?'):
                F = st.pop()
                st.pop()
                T = st.pop()
                st.pop()
                C = st.pop()
                st.append(T if C == 'T' else F)
            elif i < n:
                st.append(exp[i])
                i += 1
        return st[0]
