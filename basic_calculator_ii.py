# https://leetcode.com/problems/basic-calculator-ii/

class Solution:
    def calculate(self, s: str) -> int:
        s += '+'
        res = 0
        st = [0]
        cur_num = 0
        last_op = '+'
        for c in s:
            if c == ' ':
                continue
            if c.isdigit():
                cur_num = cur_num * 10 + int(c)
            else:
                if last_op == '+':
                    st.append(cur_num)
                elif last_op == '-':
                    st.append(-cur_num)
                elif last_op == '*':
                    x = st.pop()
                    st.append(x * cur_num)
                elif last_op == '/':
                    x = st.pop()
                    st.append(int(x / cur_num))
                else:
                    raise
                cur_num = 0
                last_op = c
        return sum(st)
