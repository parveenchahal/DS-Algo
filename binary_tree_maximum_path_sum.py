# https://leetcode.com/problems/binary-tree-maximum-path-sum/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        max_sum = root.val
        def helper(root):
            if root is None:
                return 0
            l = helper(root.left)
            r = helper(root.right)
            nonlocal max_sum
            max_sum = max(max_sum, root.val)
            max_sum = max(max_sum, root.val + max(l, r))
            max_sum = max(max_sum, l + root.val + r)
            return max(root.val, root.val + max(l, r))
        helper(root)
        return max_sum
