class TreeNode:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

class Solution:
    def count_left_right(self, root: TreeNode) -> (int, int):
        if root == None:
            return 0, 0
        lc = 1
        rc = 1
        l = root.left
        r = root.right
        
        while l != None:
            l = l.left
            lc += 1
            
        while r != None:
            r = r.right
            rc += 1
        return lc, rc
    
    def countNodes(self, root: TreeNode) -> int:
        if root == None:
            return 0
        l, r = self.count_left_right(root)
        if l == r:
            return (1 << l) - 1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
