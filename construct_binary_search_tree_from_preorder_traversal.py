# https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Using min/max range
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        def helper(root, mi, ma, q):
            if len(q) == 0:
                return
            if q[0] > mi and q[0] < root.val:
                root.left = TreeNode(q.popleft())
                helper(root.left, mi, root.val, q)
            if len(q) == 0:
                return
            if q[0] > root.val and q[0] < ma:
                root.right = TreeNode(q.popleft())
                helper(root.right, root.val, ma, q)
            
        q = deque(preorder)
        root = TreeNode(q.popleft())
        helper(root, -0x7fffffffff, 0x7fffffffff, q)
        return root

# Using stack
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(preorder[0])
        st = [root]
        for i in range(1, len(preorder)):
            node = st[-1]
            child = TreeNode(preorder[i])
            while len(st) > 0 and st[-1].val < child.val:
                node = st.pop()
            if child.val < node.val:
                node.left = child    
            else:
                node.right = child
            st.append(child)
        
        return root
        
