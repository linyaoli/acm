# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        carry = 0
        head = ListNode(0)
        cur = head

        while l1 is not None and l2 is not None:
            tmp = l1.val + l2.val + carry
            _new = ListNode(tmp % 10)
            carry = tmp / 10
            cur.next = _new
            cur = _new
            l1 = l1.next
            l2 = l2.next

        while l1 is not None:
            tmp = l1.val + carry
            _new = ListNode(tmp % 10)
            carry = tmp / 10
            cur.next = _new
            cur = _new
            l1 = l1.next

        while l2 is not None:
            tmp = l2.val + carry
            _new = ListNode(tmp % 10)
            carry = tmp / 10
            cur.next = _new
            cur = _new
            l2 = l2.next

        if carry != 0:
            _new = ListNode(carry)
            cur.next = _new

        return head.next

            
