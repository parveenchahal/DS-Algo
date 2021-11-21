# https://leetcode.com/problems/clone-binary-tree-with-random-pointer/


# Definition for Node.
# class Node:
#     def __init__(self, val=0, left=None, right=None, random=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.random = random

class Solution:
    
    def _copy(self, root, node_map):
        if root is None:
            return
        new_root = NodeCopy(root.val, None, None, root.random)
        node_map[root] = new_root
        new_root.left = self._copy(root.left, node_map)
        new_root.right = self._copy(root.right, node_map)
        return new_root
    
    def _change_random(self, root, node_map):
        if root is None:
            return
        if root.random:
            root.random = node_map[root.random]
        self._change_random(root.left, node_map)
        self._change_random(root.right, node_map)
    
    def copyRandomBinaryTree(self, root: 'Node') -> 'NodeCopy':
        node_map = {}
        new_root = self._copy(root, node_map)
        self._change_random(new_root, node_map)
        return new_root
