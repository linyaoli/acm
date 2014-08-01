# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param m, an integer
    # @param n, an integer
    # @return a ListNode
    def reverseBetween(self, head, m, n):
        step = n - m
        head_case = ListNode(-1)
        head_case.next = head
        head = head_case
        pre = head
        while m > 1:
            pre = pre.next
            m -= 1
        cur = pre.next
        post = cur.next
        if step >= 1:
            while step > 0 and post != None:
                tmp = post.next
                post.next = cur
                cur = post
                post = tmp
                step -= 1
            tmp = pre.next
            pre.next = cur
            tmp.next = post
        head_case = head
        head = head.next
        return head
