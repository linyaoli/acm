# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if not head or not head.next:
            return head

        dummy = ListNode(-1)
        dummy.next = head
        ptr = dummy
        while head and head.next:
            if head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head = head.next
                ptr.next = head.next
            else:
                ptr = ptr.next
            head = head.next

        return dummy.next
