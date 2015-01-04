# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
# Sort a linked list in O(n log n) time using constant space complexity.

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def sortList(self, head):
        if head is None or head.next is None:
            return head
        length = 0
        it = head
        while it.next is not None:
            length = length + 1
            it = it.next
        return self.merge_sort(head, length)

    def merge_sort(self, head, length):
        if length == 1:
            tmp = head
            head = head.next
            tmp.next = None
            return tmp

        leftHead = self.merge_sort(head, length / 2)
        rightHead = self.merge_sort(head, length - length / 2)
        return self.merge(leftHead, rightHead)

    def merge(self, first, second):
        head = ListNode()
        head_ori = head
        while first is not None or second is not None:
            fv = first.val
            sv = second.val
            if fv <= sv:
                head.next = first
                first = first.next
            else:
                head.next = second
                second = second.next
        head = head_ori.next
        return head
