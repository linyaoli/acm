# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        if head is None or head.next is None:
            return head
        pre = None
        p = head
        q = head.next
        head = q
        while p and q:
            p.next = q.next
            q.next = p
            if pre:
                pre.next = q
            pre = p
            p = p.next
            if p:
                q = p.next
        return head

        
