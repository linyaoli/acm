# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#  partition it such that all nodes less than x come before nodes greater than or equal to x.

class Solution:
    # @param head, a ListNode
    # @param x, an integer
    # @return a ListNode
    def partition(self, head, x):
        cur = head
        pre = None
        # find the first node which is smaller than x.
        while cur and cur.val >= x:
            pre = cur
            cur = cur.next
        if not cur:
            # if not exist
            return head
        # put the mark in the front
        if cur != head:
            pre.next = cur.next
            cur.next = head
            head = cur

        # start insertion
        pre = cur
        trav = cur.next
        while trav:
            if trav.val < x:
                if pre != cur:
                    pre.next = trav.next
                    trav.next = cur.next
                    cur.next = trav
                    cur = cur.next
                    trav = pre.next
                    continue
                else:
                    cur = cur.next
                    
            pre = pre.next
            trav = trav.next

        return head
