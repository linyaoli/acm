# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    def hasPathSum(self, root, sum):

        return self.gen(root, 0, sum)

    def gen(self, root, n, sum):
        if root is None:
            return False
        n += root.val
        if root.left is None and root.right is None:
            if n == sum:
                return True
            else:
                return False
        return self.gen(root.left, n, sum) or self.gen(root.right, n, sum)
