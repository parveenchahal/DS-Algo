# https://www.interviewbit.com/old/problems/valid-bst-from-preorder/

from collections import deque

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        st = []
        root = -0xfffffffffffffff
        for x in A:
            while len(st) > 0 and st[-1] < x:
                root = st.pop()
            if root > x:
                return 0
            st.append(x)
        return 1
