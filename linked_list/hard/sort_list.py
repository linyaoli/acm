# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
#
# Sort a linked list in O(n log n) time using constant space complexity.

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def sortList(self, head):
        p = head
        n = 0
        while p:
            p = p.next
            n += 1
        fakehead = ListNode(-1)
        fakehead.next = head
        interval = 1
        while interval < n + 1:
            pre = fakehead
            slow, fast = fakehead.next, fakehead.next
            while slow or fast:
                i = 0
                while i < interval and fast:
                    fast = fast.next
                    i += 1
                fvisit = 0
                svisit = 0
                while fvisit < interval and svisit < interval and fast and slow:
                    if fast.val < slow.val:
                        pre.next = fast
                        pre = fast
                        fast = fast.next
                        fvisit += 1
                    else:
                        pre.next = slow
                        pre = slow
                        slow = slow.next
                        svisit += 1
                while fvisit < interval and fast:
                    pre.next = fast
                    pre = fast
                    fast = fast.next
                    fvisit += 1
                while svisit < interval and slow:
                    pre.next = slow
                    pre = slow
                    slow = slow.next
                    svisit += 1
                pre.next = fast
                slow = fast
            interval *= 2
        return fakehead.next
