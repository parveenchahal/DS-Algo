# https://leetcode.com/problems/binary-tree-right-side-view


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        res = []
        q = deque([root, None])
        last_node = None
        while len(q) > 0:
            node = q.popleft()
            if node is None:
                res.append(last_node.val)
                if len(q) == 0:
                    break
                q.append(None)
                continue
            if node.left is not None:
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)
            last_node = node
        return res
