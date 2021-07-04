# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def _get_list_of_path(self, root, p, q, path):
        if root is None:
            return
        
        path.append(root)
        if root == p:
            self.p_path = list(path)
        if root == q:
            self.q_path = list(path)
            
        self._get_list_of_path(root.left, p, q, path)
        self._get_list_of_path(root.right, p, q, path)
        path.pop()
    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self._get_list_of_path(root, p, q, [])
        p_path = self.p_path
        q_path = self.q_path
        min_len = min(len(p_path), len(q_path))
        i = 0
        while i < min_len:
            if p_path[i] != q_path[i]:
                return p_path[i - 1]
            i += 1
        return p_path[i - 1]
