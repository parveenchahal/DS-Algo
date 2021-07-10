# https://leetcode.com/problems/reverse-nodes-in-k-group/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def _reverse(self, ptr, k):
        end = ptr
        pre = None
        while ptr is not None and k:
            nex = ptr.next
            ptr.next = pre
            pre = ptr
            ptr = nex
            k -= 1
        end.next = ptr
        return pre
    
    def _count(self, head):
        c = 0
        while head is not None:
            head = head.next
            c += 1
        return c
    
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if k <= 1:
            return head
        n = self._count(head)
        last_op = n - (n % k)
        new_node = None
        ptr = head
        pre = None
        i = 0
        while ptr is not None and i < last_op:
            if i % k == 0:
                x = self._reverse(ptr, k)
                if new_node is None:
                    new_node = x
                else:
                    pre.next = x
                ptr = x
            pre = ptr
            ptr = ptr.next
            i += 1
        return new_node
