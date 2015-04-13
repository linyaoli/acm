# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
# Populate each next pointer to point to its next right node.
# If there is no next right node, the next pointer should be set to NULL.
# Assume this is a perfect binary tree.

class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        if not root:
            return
        if root.left:
            root.left.next = root.right
        if root.right:
            if root.next:
                root.right.next = root.next.left
            else:
                root.right.next = None
        self.connect(root.left)
        self.connect(root.right)

        return
