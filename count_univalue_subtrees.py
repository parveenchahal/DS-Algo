# https://www.lintcode.com/problem/921/

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the given tree
    @return: the number of uni-value subtrees.
    """
    def countUnivalSubtrees(self, root):
        count = 0
        def helper(root, s):
            if root == None:
                return
            s.add(root.val)
            nonlocal count
            ls = set()
            rs = set()
            helper(root.left, ls)
            helper(root.right, rs)
            s.update(ls)
            s.update(rs)
            if len(s) == 1:
                count += 1
        helper(root, set())
        return count
