# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):
        if root is None:
            return True
        return self.check(root.left, root.right)

    def check(self, node1, node2):
        if node1 is None and node2 is None:
            return True
        elif node1 is None and node2 is not None:
            return False
        elif node1 is not None and node2 is None:
            return False
        if node1.val != node2.val:
            return False
        return self.check(node1.left, node2.right) and self.check(node1.right, node2.left)
