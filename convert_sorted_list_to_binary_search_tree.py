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
        if not head: return head
        self.node = head
        head = head.next
        end = 0
        while head: end += 1; head = head.next
        return self.helper(0, end)

    def helper(self, start, end):
        if start > end: return None
        mid = (start + end) /2
        left = self.helper(start, mid - 1)
        parent = TreeNode(self.node.val)
        parent.left = left
        # after divide the list into two parts, we move the node to the next one,
        # it will represent the head of the second half list.
        self.node = self.node.next
        parent.right = self.helper(mid + 1, end)
        return parent
