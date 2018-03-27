# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        if not head:
            return head
        slow = fast = head
        count = 0

        while fast and count < n:
            fast = fast.next
            count += 1
        if count == n and not fast:
            head = head.next
            return head
        while fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next

        return head
