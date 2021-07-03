# https://leetcode.com/problems/balanced-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        balanced = True
        def helper(root):
            nonlocal balanced
            if root is None:
                return 0
            if not balanced:
                return 0
            l = helper(root.left)
            r = helper(root.right)
            if abs(l - r) > 1:
                balanced = False
            return 1 + max(l, r)
        helper(root)
        return balanced
