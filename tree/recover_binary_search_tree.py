"""
Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.

"""
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a tree node
    prev = None
    p1 = None
    p2 = None

    def inOrder(self, root):
        if not root: return
        self.inOrder(root.left)
        if not self.prev:
            self.prev = root
        else:
            if root.val <= self.prev.val:
                if not self.p1:
                    self.p1 = self.prev
                self.p2 = root
            self.prev = root
        self.inOrder(root.right)

    def recoverTree(self, root):
        self.inOrder(root)
        self.p1.val, self.p2.val = self.p2.val, self.p1.val
