# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return []
        res = []
        def s(root):
            if root is None:
                res.append(None)
                return
            res.append(root.val)
            s(root.left)
            s(root.right)
        s(root)
        return res
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        n = len(data)
        if n <= 0:
            return
        i = 0
        def d():
            nonlocal i
            if i >= n:
                return
            x = data[i]
            i += 1
            if x is None:
                return
            root = TreeNode(x)
            root.left = d()
            root.right = d()
            return root
        root = d()
        return root
      
