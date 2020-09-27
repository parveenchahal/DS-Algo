#
# https://www.interviewbit.com/problems/generate-all-parentheses/
#

from collections import deque
    
def is_valid_parentheses(A):
    st = deque()
    
    b = {
        '}': '{',
        ']': '[',
        ')': '(',
        '{': None,
        '[': None,
        '(': None
    }
    
    for x in A:
        if len(st) <= 0:
            st.append(x)
        else:
            peek = st.pop()
            if b[x] != peek:
                st.append(peek)
                st.append(x)
    return 1 if len(st) == 0 else 0


print(is_valid_parentheses("()[]{}}"))