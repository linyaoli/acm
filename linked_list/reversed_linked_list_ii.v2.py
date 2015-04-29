# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param m, an integer
    # @param n, an integer
    # @return a ListNode
    def reverseBetween(self, head, m, n):
        if not head or not head.next:
            return head
        fakehead = ListNode(-1)
        fakehead.next = head
        node = fakehead
        i = 1
        while i < m:
            node = node.next
            i += 1

        p = node.next
        q = p.next
        if q:
            r = q.next
        while i < n:
            q.next = p
            p = q
            q = r
            if r:
                r = r.next
            i += 1

        # now p is the head of reversed part, node.next is the tail of reversed part.
        tmp = node.next
        node.next = p
        tmp.next = q

        return fakehead.next
