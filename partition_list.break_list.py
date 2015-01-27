# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param x, an integer
    # @return a ListNode
    def partition(self, head, x):
        iterA = listA = ListNode(-1)
        iterB = listB = ListNode(-1)
        while head:
            if head.val < x:
                iterA.next = head
                iterA = iterA.next
                head = head.next
            else:
                iterB.next = head
                iterB = iterB.next
                head = head.next
        iterA.next = listB.next
        iterB.next = None

        return listA.next
