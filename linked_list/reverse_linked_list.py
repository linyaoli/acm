# iteration
def reverse(head):
    if not head or not head.next:
        return head
    p = head
    q = p.next
    p.next = None
    while q:
        r = q.next
        q.next = p
        p = q
        q = r
        if r:
            r = r.next
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
