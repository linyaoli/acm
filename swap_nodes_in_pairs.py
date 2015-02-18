# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        if not head or not head.next:
            return head
        p = None
        q = head
        r = head.next
        head = head.next

        while q and r:
            q.next = r.next
            r.next = q
            if p:
                p.next = r
            p = q
            q = p.next
            if q:
                r = q.next

        return head
