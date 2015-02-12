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
        res = self.helper(root)
        if res == -1:
            return False
        return True

    def helper(self, root):
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        left_depth = self.helper(root.left)
        if left_depth == -1:
            return -1
        right_depth = self.helper(root.right)
        if right_depth == -1:
            return -1
        if abs(left_depth - right_depth) <= 1:
            return max(left_depth, right_depth) + 1
        else:
            return -1
