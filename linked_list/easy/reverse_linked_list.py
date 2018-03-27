# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
        if not head or not head.next: return head
        p = head
        q = head.next
        p.next = None
        r = q.next
        while p and q:
            q.next = p
            p = q
            q = r
            if q: r = q.next

        return p

class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

# recursion

def reverseR(pre, cur):
    if not cur:
        return pre
    next = cur.next
    cur.next = pre
    return reverseR(cur, next)


head = ListNode(10)
k = head
for i in xrange(9):
    tmp = ListNode(i)
    k.next = tmp
    k = k.next
k.next = None

#k = reverse(head)
k = reverseR(None, head)

while k:
    print k.val
    k = k.next
