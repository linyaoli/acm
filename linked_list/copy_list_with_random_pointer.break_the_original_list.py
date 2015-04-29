# Definition for singly-linked list with a random pointer.
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        if not head: return head
        cphead = RandomListNode(head.label)
        p = cphead
        q = head.next
        while q:
            t = RandomListNode(q.val)
            p.next = t
            p = p.next
            q = q.next

        p = cphead
        q = head
        r = head.next
        while p and q:
            p.random = q
            q.next = p
            q = r
            if q:
                r = q.next
            p = p.next

        p = cphead
        while p:
            p.random = p.random.random.next
            p = p.next

        return cphead
