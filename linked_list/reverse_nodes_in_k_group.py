# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} k
    # @return {ListNode}
    def reverseKGroup(self, head, k):
        dummy = ListNode(-1)
        dummy.next = head
        head = dummy
        while head:
            i = 0
            end = head
            while i < k and end.next:
                end = end.next
                i += 1
            if i < k: return dummy.next
            start, tail = self.reverse(head, head.next, end)
            tmp = head.next
            head.next.next = tail
            head.next = start
            head = tmp

        return dummy.next

    def reverse(self, prev, cur, end):
        if end == prev or not cur: return prev, cur
        tmp = cur.next
        cur.next = prev
        return self.reverse(cur, tmp, end)


dummy = ListNode(-1)
h = dummy
for i in [1,2,3,4,5,6,7,8,9]:
    h.next = ListNode(i)
    h = h.next

sol = Solution()
k = sol.reverseKGroup(dummy.next, 5)

while k:
    print k.val,
    k = k.next
