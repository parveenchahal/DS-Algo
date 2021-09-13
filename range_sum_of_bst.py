# https://leetcode.com/problems/range-sum-of-bst/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        res = 0
        def helper(root, low, high):
            if root is None:
                return
            nonlocal res
            if root.val >= low and root.val <= high:
                res += root.val
            if root.val >= low:
                helper(root.left, low, high)
            if root.val <= high:
                helper(root.right, low, high)
        helper(root, low, high)
        return res
