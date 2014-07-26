# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        if root is None:
            return
        p = root.next
        while p is not None:
            if p.left is not None:
                p = p.left
                break
            if p.right is not None:
                p = p.right
                break
            p = p.next
        if root.right is not None:
            root.right.next = p
        if root.left is not None:
            if root.right is not None:
                root.left.next = root.right
            else:
                root.left.next = p
        self.connect(root.right)
        self.connect(root.left)
            
