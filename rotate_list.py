# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def rotateRight(self, head, k):
        if head is None or k == 0:
            return head
        _len = 1
        p = head
        while p.next is not None:
            p = p.next
            _len += 1
        k = _len - k % _len
        p.next = head
        step = 0
        while step < k:
            p = p.next
            step += 1
        head = p.next
        p.next = None
        return head

            
