# https://leetcode.com/problems/merge-k-sorted-lists/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def _merge(self, head1, head2):
        # Added a dummy node
        ptr = head = ListNode(None)
        while head1 is not None and head2 is not None:
            if head1.val <= head2.val:
                ptr.next = head1
                head1 = head1.next
            else:
                ptr.next = head2
                head2 = head2.next
            ptr = ptr.next
        if head1 is not None:
            ptr.next = head1
        else:
            ptr.next = head2
        return head.next

    
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if len(lists) == 0:
            return
        q = deque(lists)
        while len(q) > 1:
            x = q.popleft()
            y = q.popleft()
            q.append(self._merge(x, y))
        return q[0] if len(q) > 0 else None
