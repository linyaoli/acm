# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    sum = 0
    def sumNumbers(self, root):
        self.gen(root, self.sum, 0)
        return self.sum

    def gen(self, root, sum, path):
        if not root: return 0
        path = path * 10 + root.val
        if root.left is None and root.right is None:
            self.sum += path
            return
        self.gen(root.left, self.sum, path)
        self.gen(root.right, self.sum, path)

class AlternativeSolution:
    # @param root, a tree node
    # @return an integer
    def sumNumbers(self, root):
        return self.gen(root, 0)

    def gen(self, root, path):
        if not root:
            return 0
        path = path * 10 + root.val
        if not root.left and not root.right:
            return path
        else:
            return self.gen(root.left, path) + \
            self.gen(root.right, path)
