# https://leetcode.com/problems/reverse-nodes-in-k-group/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def _reverse(self, head, end):
        pre = end
        while head != end:
            next = head.next
            head.next = pre
            pre = head
            head = next
        return pre
    
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
