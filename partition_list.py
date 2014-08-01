# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param x, an integer
    # @return a ListNode
    def partition(self, head, x):
        node = ListNode(x - 1)
        node.next = head
        head = node
        # find the first smaller node
        pre = None
        while node is not None and node.val < x:
            pre = node
            node = node.next
        if node is not None:
            cur = pre
            while node is not None:
                if node.val < x:
                    tmp = cur.next
                    pre.next = node.next
                    cur.next = node
                    cur = node
                    node.next = tmp
                    node = pre
                pre = node
                node = node.next
        tmp = head
        head = head.next
        return head
          
