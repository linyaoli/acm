#!/usr/bin/python


class ListNode:
    def _init_(self, x):
        self.val = x
        self.next = None


class Solution:
    def sortList(self, head):
        if head is None:
            return None
        length = 0
        it = head
        while it.next is not None:
            length = length + 1
            it = it.next

        if length == 1:
            return head
        return self.merge_sort(head, length)

    def merge_sort(self, head, length):

        leftHead = self.merge_sort(head, length / 2)
        rightHead = self.merge_sort(head, length - length / 2)
        return self.merge(leftHead, rightHead)

    def merge(self, first, second):
        head = ListNode()
        head_ori = head
        while first is not None and second is not None:
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
