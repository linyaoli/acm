# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import sys

class Solution:
    # @param root, a tree node
    # @return an integer

    def minDepth(self, root):
        if root is None:
            return 0
        return self.gen(root)

    def gen(self, root):
        if root is None:
            return 0
        left = self.gen(root.left)
        right = self.gen(root.right)
        if left == 0 and right == 0:
            return 1
        elif left == 0:
            left = sys.maxint
        elif right == 0:
            right = sys.maxint
        return min(left, right) + 1
