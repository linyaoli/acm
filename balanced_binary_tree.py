# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean

    def isBalanced(self, root):
        if root is None:
            return True
        val = self.getBalance(root)
        if val == -1:
            return False
        return True
    def getBalance(self, root):
        if root is None:
            return 0
        left = self.getBalance(root.left)
        if left == -1:
            return -1
        right = self.getBalance(root.right)
        if right == -1:
            return -1
        if abs(left - right) > 1:
            return -1
        return max(left, right) + 1
