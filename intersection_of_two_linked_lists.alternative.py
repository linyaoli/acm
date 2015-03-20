# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
"""
To see why the above trick would work, consider the following two lists:
A = {1,3,5,7,9,11} and B = {2,4,9,11}, which are intersected at node '9'.
 Since B.length (=4) < A.length (=6), pB would reach the end of the merged list first,
 because pB traverses exactly 2 nodes less than pA does. By redirecting pB to head A,
 and pA to head B, we now ask pB to travel exactly 2 more nodes than pA would. So in the
 second iteration, they are guaranteed to reach the intersection node at the same time.
"""
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
            # start again from another list's head.
            if not pA:
                pA = headB
            if not pB:
                pB = headA
            #locate the tail
            if not pA.next:
                tailA = pA
            if not pB.next:
                tailB = pB
            if tailA and tailB and tailA != tailB:
                return None
            ########
            if pA == pB:
                return pA
            pA = pA.next
            pB = pB.next
