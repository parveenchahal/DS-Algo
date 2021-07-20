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
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if root is None:
            return
        def _tree_to_doubly_list(root):
            if root == None:
                return
            l = root.left
            r = root.right
            _tree_to_doubly_list(l)
            _tree_to_doubly_list(r)
            if l is not None:
                while l.right != None:
                    l = l.right
                root.left = l
                l.right = root
            if r is not None:
                while r.left != None:
                    r = r.left
                root.right = r
                r.left = root
        
        _tree_to_doubly_list(root)
        while root.left != None:
            root = root.left
        
        ptr = root
        while ptr.right != None:
            ptr = ptr.right
        
        ptr.right = root
        root.left = ptr
        
        return root
