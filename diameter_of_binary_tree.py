# https://leetcode.com/problems/diameter-of-binary-tree/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        max_dist = 0
        def _diameter_of_binary_tree(root):
            nonlocal max_dist
            if root is None:
                return 0
            l = _diameter_of_binary_tree(root.left)
            r = _diameter_of_binary_tree(root.right)
            max_dist = max(max_dist, l + r + 1)
            return 1 + max(l, r)
        _diameter_of_binary_tree(root)
        return max_dist - 1
