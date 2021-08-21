# https://leetcode.com/problems/longest-valid-parentheses/

# Using extra memory(stack)
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        st = [-1]
        res = 0
        for i in range(n):
            c = s[i]
            if c == '(':
                st.append(i)
            else:
                if len(st) > 1 and s[st[-1]] == '(':
                    st.pop()
                    res = max(res, i - st[-1])
                else:
                    st = [i]
        res = max(res, n - 1 - st[-1])
        return res

    
# Without extra memory; space: O(1)
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        res = 0
        left = right = 0
        for i in range(n):
            c = s[i]
            if c == '(':
                left += 1
            else:
                right += 1
            if right > left:
                left = right = 0
            elif left == right:
                res = max(res, left + right)
        
        left = right = 0
        for i in range(n - 1, -1, -1):
            c = s[i]
            if c == '(':
                left += 1
            else:
                right += 1
            if left > right:
                left = right = 0
            elif left == right:
                res = max(res, left + right)
        return res
