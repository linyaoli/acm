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
        p = head
        q = head.next
        r = q.next
        head = head.next
        while q is not None:
            q.next = p
            if r is None or r.next is None:
                p.next = r
                break
            else:
                p.next = r.next
            p = r
            q = p.next
            r = q.next


        return head

        
