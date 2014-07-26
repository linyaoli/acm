# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        if head is None:
            return None
        fast = head
        slow = head
        count = 0

        while fast != None and count < n:
            fast = fast.next
            count += 1
        if count == n and fast is None:
            head = head.next
            return head
        while fast.next is not None:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next

        return head
        
