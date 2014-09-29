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
        if head is None:
            return None
        cur = head
        while cur is not None:
            post = RandomListNode(cur.label)
            post.next = cur.next
            cur.next = post
            cur = post.next

        # copy random pointer
        cur = head
        while cur is not None:
            post = cur.next
            if cur.random is not None:
                post.random = cur.random.next
            cur = post.next
        #
        cur = head
        dup = head
        if head is not None:
            dup = head.next
        while cur is not None:
            tmp = cur.next
            cur.next = tmp.next
            if tmp.next is not None:
                tmp.next = tmp.next.next
            cur = cur.next
        return dup

            
