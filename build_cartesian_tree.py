# https://www.interviewbit.com/problems/inorder-traversal-of-cartesian-tree/

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self) -> str:
        l = self.left if self.left is not None else None
        r = self.right if self.right is not None else None
        return "{" + f'self: {self.val}, left: {l}, right: {r}' + "}"

class Solution:
    # @param A : list of integers
    # @return the root node in the tree

    def _find_max_index(self, A, i, j):
        index = i
        val = A[i]
        for k in range(i + 1, j + 1):
            if A[k] > val:
                index = k
                val = A[k]
        return index

    def _buildTree(self, A, st, ed):
        if st > ed:
            return
        m = self._find_max_index(A, st, ed)
        r = TreeNode(A[m])
        if st < m:
            r.left = self._buildTree(A, st, m - 1)
        if m < ed:
            r.right = self._buildTree(A, m + 1, ed)
        return r


    def buildTree(self, A):
        return self._buildTree(A, 0, len(A) - 1)

r = Solution().buildTree([2,1,3])
print(r)

r = Solution().buildTree([5, 10, 40, 30, 28 ])
print(r)