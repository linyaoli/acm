# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param num, a list of integers
    # @return a tree node
    def sortedArrayToBST(self, num):
        if num == [] : return None
        return self.helper(num, 0, len(num) - 1)
        
    def helper(self, num, start, end):
        if start > end: return None
        mid = (end + start) / 2
        left = self.helper(num, start, mid - 1)
        right = self.helper(num, mid + 1, end)
        mid_node = TreeNode(num[mid])
        mid_node.left = left
        mid_node.right = right
        return mid_node
