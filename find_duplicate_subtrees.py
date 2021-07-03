# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        s = set()
        subtrees = {}
        def helper(root):
            nonlocal s, subtrees
            if root is None:
                return
            l = helper(root.left)
            r = helper(root.right)
            x = (l if l is not None else 'L') + ',' + str(root.val) + ',' + (r if r is not None else 'R')
            if x in s:
                subtrees[x] = root
            else:
                s.add(x)
            return x
        helper(root)
        return subtrees.values()

      
#      0
#     / \
#    0   0
#   /     \
#  0       0
#           \
#            0
# There is only one duplicate subtree
