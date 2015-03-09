# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# brute force : merge lists one by one
#               O(nk2) runtime, O(1) space
#           why? merge 2 lists of length n to 2n -> next time merge a 2n list and a n list.
#                After this, we have n + 2n + 3n + ... + kn = O(nk2)

class Solution:
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, lists):
        if lists == []: return None
        end = len(lists) - 1
        while end > 0:
            begin = 0
            while begin < end :
                lists[begin] = self.mergeTwoLists(lists[begin], lists[end])
                begin += 1
                end -= 1
        return lists[0]


    def mergeTwoLists(self, l1, l2):
        if not l1 or not l2:
            return l1 or l2
        dummy = ListNode(-1)
        trav = dummy
        while l1 and l2:
            if l1.val < l2.val:
                trav.next = l1
                l1 = l1.next
            else:
                trav.next = l2
                l2 = l2.next
            trav = trav.next

        if l1: trav.next = l1
        if l2: trav.next = l2
        return dummy.next
