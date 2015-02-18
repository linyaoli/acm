# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a list node
    # @return a tree node

    def sortedListToBST(self, head):
        if head is None:
            return None
        n = 0
        iter = head
        while iter is not None:
            n += 1
            iter = iter.next
        #need a global var to mark
        self.node = head
        return self.sort(0, n - 1)

    def sort(self, start, end):
        if start > end:
            return None

        mid = start + (end - start) / 2
        left = self.sort(start, mid - 1)
        parent = TreeNode(self.node.val)
        parent.left = left
        self.node = self.node.next
        parent.right = self.sort(mid + 1, end)
        return parent
