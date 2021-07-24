# https://leetcode.com/problems/decode-string/


class Solution:
    def decodeString(self, s: str) -> str:
        n = len(s)
        st = []
        for i in range(n):
            if s[i] != ']':
                if s[i] >= '0' and s[i] <= '9' and len(st) > 0 and st[-1] >= '0' and st[-1] <= '9':
                    st[-1] += s[i]
                else:
                    st.append(s[i])
            else:
                rs = ''
                while len(st) > 0 and st[-1] != '[':
                    rs = st.pop() + rs
                st.pop()
                rf = ''
                while len(st) > 0 and st[-1] >= '0' and st[-1] <= '9':
                    rf = st.pop() + rf
                t = rs * int(rf)
                for c in t:
                    st.append(c)
        return ''.join(st)
