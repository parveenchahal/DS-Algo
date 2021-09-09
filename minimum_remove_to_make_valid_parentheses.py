# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

# Method 1 Using stack
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
