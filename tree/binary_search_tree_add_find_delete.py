# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def add(self, val, root):
        if not root: return None

        if val < root.val:
            child = self.add(val, root.left)
            if not child:
                node = TreeNode(val)
                root.left = node
        else:#if val >= root.val:
            child = self.add(val, root.left)
            if not child:
                node = TreeNode(val)
                root.right = node

        return

    def find(self, val, root):
        if not root: return False
        node = None
        if val < root.val:
            node = self.find(val, root.left)
        elif val > root.val:
            node = self.find(val, root.right)
        else:
            return True
        if not node:
            return False

    def delete(self, val, root, prev, l_r):
        if not root: return None
        if val < root.val:
            self.delete(val, root.left, root, 1)
        elif val > root.val:
            self.delete(val, root.right, root, 0)
        else:
            if l_r == 1:
                prev.left = root.left
                n = root
                while n.right:
                    n = n.right
                n.right = root.right
            else:
                prev.right = root.right
                n = root
                while n.left:
                    n = n.left
                n.left = root.right
        return
