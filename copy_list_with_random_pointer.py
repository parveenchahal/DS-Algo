# https://leetcode.com/problems/copy-list-with-random-pointer/

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return
        
        ptr = head
        while ptr != None:
            new_node = Node(ptr.val, ptr.next, ptr.random)
            ptr.next = new_node
            ptr = new_node.next
        
        ptr = head
        while ptr != None:
            c = ptr.next
            if c.random:
                c.random = c.random.next
            ptr = ptr.next.next
        
        head2 = head.next
        ptr = head
        while ptr != None:
            c = ptr.next
            ptr.next = c.next
            if c.next:
                c.next = c.next.next
            ptr = ptr.next
        
        return head2
