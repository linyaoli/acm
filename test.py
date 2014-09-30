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
        if head is None:
            return head
        else:
            p = head
        counter = 0
        pre = None
        tail = None
        new_head = None
        while p is not None:
            if k == counter:
                pre = p
                new_head = pre.next
            if p.next is None:
                tail = p
            counter += 1
            p = p.next
        tail.next = head
        pre.next = None

        return new_head

            
