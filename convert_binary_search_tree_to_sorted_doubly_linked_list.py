# https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/

"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution:
    def _tree_to_doubly_list(self, root):
        if root is None:
            return
        self._tree_to_doubly_list(root.left)
        self._tree_to_doubly_list(root.right)
        
        l = root.left
        r = root.right
        
        if l is not None:
            while l.right:
                l = l.right
            root.left = l
            l.right = root
        
        if r is not None:
            while r.left:
                r = r.left
            r.left = root
            root.right = r
    
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if root is None:
            return
        
        self._tree_to_doubly_list(root)
        
        while root.left:
            root = root.left
        last = root
        
        while last.right:
            last = last.right
        
        last.right = root
        root.left = last
        
        return root
