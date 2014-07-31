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
        return self.sort(head, 0, n - 1)

    def sort(self, node, start, end):
        if start > end:
            return None
        mid = start + (end - start) / 2
        left = self.sort(node, start, mid - 1)
        parent = TreeNode(node.val)
        parent.left = left
        node = node.next
        parent.right = self.sort(node, mid + 1, end)
        return parent

        
