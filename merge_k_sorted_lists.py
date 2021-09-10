# https://leetcode.com/problems/merge-k-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def _merge(head1, head2):
        if head1 is None:
            return head2
        if head2 is None:
            return head1
        head = None
        if head1.val <= head2.val:
            head = head1
            head1 = head1.next
        else:
            head = head2
            head2 = head2.next
        
        ptr = head
        while head1 is not None and head2 is not None:
            if head1.val <= head2.val:
                ptr.next = head1
                head1 = head1.next
            else:
                ptr.next = head2
                head2 = head2.next
            ptr = ptr.next
        
        while head1 is not None:
            ptr.next = head1
            ptr = ptr.next
            head1 = head1.next
            
        while head2 is not None:
            ptr.next = head2
            ptr = ptr.next
            head2 = head2.next
        return head


    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if len(lists) == 0:
            return
        q = deque(lists)
        while len(q) > 1:
            new_q = deque()
            while len(q) > 1:
                x = q.popleft()
                y = q.popleft()
                t = Solution._merge(x, y)
                if t is not None:
                    new_q.append(t)
            if len(q) == 1:
                new_q.append(q.popleft())
            q = new_q
        
        return q.popleft() if len(q) > 0 else None
