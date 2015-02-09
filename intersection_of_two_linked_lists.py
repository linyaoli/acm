# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        if headA is None or headB is None:
            return None
        inter_node = None
        iterA = headA
        iterB = headB
        lengthA = 0
        lengthB = 0
        while iterA.next:
            iterA = iterA.next
            lengthA += 1
        while iterB.next:
            iterB = iterB.next
            lengthB += 1
        if iterA != iterB:
            return None
        else:
            iterA = headA
            iterB = headB
            if lengthA < lengthB:
                iterA, iterB = iterB, iterA
            for i in xrange(abs(lengthA - lengthB)):
                iterA = iterA.next
            while iterA != iterB:
                iterA = iterA.next
                iterB = iterB.next
            return iterA
