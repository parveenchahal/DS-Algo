# https://leetcode.com/problems/basic-calculator-iii/


class Solution:
    
    PRECEDENCE = {
        '+': 0,
        '-': 0,
        '*': 1,
        '/': 1
    }
    
    def _infix_to_postfix(self, s):
        s = f'({s})'
        postfix = []
        st = []
        cur_num = ''
        for c in s:
            if c.isdigit():
                cur_num += c
                continue
            if cur_num != '':
                postfix.append(int(cur_num))
            
            if c in ('+', '-', '*', '/'):
                while len(st) > 0 and st[-1] != '(' and self.PRECEDENCE[st[-1]] >= self.PRECEDENCE[c]:
                    postfix.append(st.pop())
                st.append(c)
            elif c == '(':
                st.append(c)
            else:
                while st[-1] != '(':
                    postfix.append(st.pop())
                st.pop()
            cur_num = ''
        return postfix
    
    def _op(self, a, b, op):
        if op == '+': return a + b
        if op == '-': return a - b
        if op == '*': return a * b
        if op == '/': return int(a / b)
    
    def _process_postfix(self, postfix):
        st = []
        for x in postfix:
            if x in ('+', '-', '*', '/'):
                b = st.pop()
                a = st.pop()
                st.append(self._op(a, b, x))
            else:
                st.append(x)
        return st[0]
    
    def calculate(self, s: str) -> int:
        postfix = self._infix_to_postfix(s)
        return self._process_postfix(postfix)
