# https://www.lintcode.com/problem/921/


# Method 1 (Using Sets)
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

# Method 2 (Without using Sets)
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
        def helper(root):
            nonlocal count
            if root == None:
                return 0
            c1 = helper(root.left)
            c2 = helper(root.right)
            c = 1
            if root.left is not None and root.val != root.left.val:
                c += 1
            c = max(c, c1)
            if root.right is not None and root.val != root.right.val:
                c += 1
            c = max(c, c2)
            if c == 1:
                count += 1
            return c
        helper(root)
        return count
