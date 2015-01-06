# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        if not (headA and headB):
            return None
        pA = headA
        pB = headB
        tailA = None
        tailB = None
        while True:
            if not pA:
                pA = headB
            if not pB:
                pB = headA
            if not pA.next:
                tailA = pA
            if not pB.next:
                tailB = pB
            if tailA and tailB and tailA != tailB:
                return None
            if pA == pB:
                return pA
            pA = pA.next
            pB = pB.next
