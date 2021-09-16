# https://leetcode.com/problems/decode-string/


BRAC = 0
INT = 1
ABC = 2

class Solution:
    def add(st, typ, val_arr):
        if len(st) <= 0 or typ != st[-1][0]:
            st.append([typ, []])
        st[-1][1].extend(val_arr)
        
    def remove(st):
        abc = []
        rf = ['1']
        if len(st) > 0 and st[-1][0] == ABC:
            _, abc = st.pop()
        if len(st) > 0 and st[-1][0] == BRAC:
            st.pop()
        if len(st) > 0 and st[-1][0] == INT:
            _, rf = st.pop()
        rf = int(''.join(rf))
        return abc * rf
    
    def decodeString(self, s: str) -> str:
        n = len(s)
        st = []
        for i in range(n):
            c = s[i]
            if c >= '0' and c <= '9':
                Solution.add(st, INT, [c])
            elif c >= 'a' and c <= 'z':
                Solution.add(st, ABC, [c])
            elif c == '[':
                Solution.add(st, BRAC, [c])
            else:
                t = Solution.remove(st)
                Solution.add(st, ABC, t)
        return ''.join(st[0][1])
