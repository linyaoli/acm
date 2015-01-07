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
        node = head
        while node.next:
            if node.val == node.next.val:
                node.next = node.next.next
                continue

            node = node.next

        return head

        
