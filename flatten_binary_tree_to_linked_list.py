# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return nothing, do it in place
    def flatten(self, root):
        if not root:
            return
        self.flatten(root.left)
        self.flatten(root.right)
        if root.left:
            node = root.left
            while node.right:
                node = node.right
            node.right = root.right
            root.right = root.left
            root.left = None
