# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

# Method 1 using two pass
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        n = len(s)
        idx_remove = set()
        bal = 0
        for i in range(n):
            c = s[i]
            if c == '(':
                bal += 1
            elif c == ')':
                bal -= 1
            if bal < 0:
                idx_remove.add(i)
                bal = 0
        
        bal = 0
        for i in range(n - 1, -1, -1):
            c = s[i]
            if c == ')':
                bal += 1
            elif c == '(':
                bal -= 1
            if bal < 0:
                idx_remove.add(i)
                bal = 0
        
        res_str = []
        for i,c in enumerate(s):
            if i not in idx_remove:
                res_str.append(c)
        return ''.join(res_str)


# Method 2 Using stack
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        idx_remove = set()
        st = []
        for i,c in enumerate(s):
            if c not in ['(', ')']:
                continue
            if c == '(':
                st.append(i)
            elif len(st) <= 0:
                idx_remove.add(i)
            else:
                st.pop()
        for x in st:
            idx_remove.add(x)
        res_str = []
        for i,c in enumerate(s):
            if i not in idx_remove:
                res_str.append(c)
        return ''.join(res_str)
