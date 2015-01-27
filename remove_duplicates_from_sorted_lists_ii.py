# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if not head or not head.next:
            return head

        f = ListNode(-1)
        f.next = head
        slow = f
        fast = f.next
        while fast and fast.next:
            tmp = fast.val
            fast = fast.next
            deleted = 0
            while fast and fast.val == tmp:
                fast = fast.next
                deleted = 1
            if deleted:
                slow.next = fast
            else:
                slow = slow.next

        return f.next
