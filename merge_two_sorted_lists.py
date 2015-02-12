# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        if not l1 or not l2:
            return l1 or l2
        fakehead = ListNode(-1)
        trav = fakehead
        while l1 or l2:
            if not l1:
                trav.next = l2
                l2 = l2.next
            elif not l2:
                trav.next = l1
                l1 = l1.next
            elif l1.val <= l2.val:
                trav.next = l1
                l1 = l1.next
            else:
                trav.next = l2
                l2 = l2.next
            trav = trav.next

        return fakehead.next
