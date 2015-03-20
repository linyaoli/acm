# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# assume a is distance before intersection node.
# assume b is distance slow's walking distance after intersection node.
# assume c is remaining distance in the cycle except for b.

# walking distance of slow = a + b.
# walking distance of fast = a + b + c + b
# thus, 2 * (a + b) = a + b + c + b
# a = c

class Solution:
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        slow = head
        fast = head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        if fast and fast.next:
            while head != slow:
                slow = slow.next
                head = head.next
            return head
        else:
            return None
