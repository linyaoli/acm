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
        if not root: return 0
        return self.gen(root)

    def gen(self, root):
        if not root: return 0
        left = self.gen(root.left)
        right = self.gen(root.right)
        if left == 0 and right == 0:
            return 1
        elif left == 0:
            left = sys.maxint
        elif right == 0:
            right = sys.maxint
        return min(left, right) + 1

    def helper(self, root, n): # solution 2
        if not root: return 0
        n += 1
        if not root.left and not root.right:
            self.depth = min(self.depth, n)
        else:
            self.helper(root.left, n)
            self.helper(root.right, n)

    def helper2(self, roor):
        if no root: return 0
        if not root.left:
            return self.helper2(root.right) + 1
        if not root.right:
            return self.helper2(root.left) + 1
        return min(self.helper2(root.left), self.helper2(root.right)) + 1
