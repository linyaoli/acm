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
        cur = head
        while cur:
            tmp = RandomListNode(cur.label)
            tmp.next = cur.next
            cur.next = tmp
            cur = tmp.next
        #copy random pointer
        cur = head
        while cur:
            tmp = cur.next
            if cur.random:
                tmp.random = cur.random.next
            cur = tmp.next
        # decouple
        cur = head
        dup = head.next
        while cur:
            tmp = cur.next
            cur.next = tmp.next
            if tmp.next:
                tmp.next = tmp.next.next
            cur = cur.next
        return dup
