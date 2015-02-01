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
        if not head or k == 0:
            return head
        n = 1
        p = head
        while p.next:
            p = p.next
            n += 1
        k = n - k % n # possibility of rotating more than length
        p.next = head
        step = 0
        while step < k:
            p = p.next
            step += 1
        head = p.next
        p.next = None
        return head
