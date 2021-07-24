# https://leetcode.com/problems/boundary-of-binary-tree/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        res = []
        
        def left_side(root):
            if root is None:
                return
            if root.left is None and root.right is None:
                return
            res.append(root.val)
            if root.left is None:
                left_side(root.right)
            left_side(root.left)
            
        def leaf_nodes(root):
            if root is None:
                return
            if root.left is None and root.right is None:
                res.append(root.val)
            leaf_nodes(root.left)
            leaf_nodes(root.right)
        
        def right_side(root):
            if root is None:
                return
            if root.left is None and root.right is None:
                return
            if root.right is None:
                right_side(root.left)
            right_side(root.right)
            res.append(root.val)
        
        res.append(root.val)
        left_side(root.left)
        leaf_nodes(root.left)
        leaf_nodes(root.right)
        right_side(root.right)
        return res
