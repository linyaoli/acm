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
        if num == []:
            return None
        return self.construction(0, len(num) - 1, num)

    def construction(self, start, end, num):
        if start > end:
            return None
        mid = (start + end) / 2
        left = self.construction(start, mid - 1, num)
        root = TreeNode(num[mid])
        right = self.construction(mid + 1, end, num)

        root.left = left
        root.right = right

        return root




        
