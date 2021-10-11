# https://leetcode.com/problems/reverse-nodes-in-k-group/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def _reverse(self, head, end):
        new_head = head
        ptr = head.next
        new_head.next = end
        while ptr != end:
            next = ptr.next
            ptr.next = new_head
            new_head = ptr
            ptr = next
        return new_head
    
    def _find_end_node(self, ptr, k):
        end = ptr
        i = 0
        while i < k:
            if end is None:
                return None, False
            end = end.next
            i += 1
        return end, True
    
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if k <= 1:
            return head
        end, found = self._find_end_node(head, k)
        if not found:
            return head
        
        pre = head
        head = self._reverse(head, end)
        ptr = end
        while ptr != None:
            end, found = self._find_end_node(ptr, k)
            if not found:
                return head
            pre.next = self._reverse(ptr, end)
            pre = ptr
            ptr = end
        return head
