# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        def _flatten(root):
            if root is None:
                return
            
            l = root.left
            r = root.right
            
            _flatten(l)
            if l != None:
                root.left = None
                root.right = l
                while l.right != None:
                    l = l.right
                l.right = r
            
            _flatten(r)
        _flatten(root)
