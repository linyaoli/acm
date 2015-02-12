# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        if not (l1 and l2):
            return l1 or l2

        if l1.val > l2.val:
            l1, l2 = l2, l1
        head = l1

        while l1.next and l2:
            if l1.next.val > l2.val:
                p = l2
                l2 = l2.next
                p.next = l1.next
                l1.next = p
                l1 = p
            else:
                l1 = l1.next
        while l1.next:
            l1 = l1.next
        l1.next = l2

        return head
