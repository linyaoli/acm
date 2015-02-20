# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def insertionSortList(self, head):
        if not head or not head.next:
            return head
        node = head # mark as the end of insertion
        while node.next:
            cur = node.next
            # if larger than end of the list
            if cur.val >= node.val:
                node = node.next
                continue
            # head has to be moved if not larger than the end of the list
            node.next = cur.next
            # if smaller than the beginning of the list
            if cur.val <= head.val:
                cur.next = head
                head = cur
            else:
                pos = self.findInsertPos(head, cur)
                cur.next = pos.next
                pos.next = cur
        return head

    def findInsertPos(self, head, node):
        pos = head
        while head and node.val > head.val:
            pos = head
            head = head.next

        return pos
