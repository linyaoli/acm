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
        if not root: return False
        n += root.val
        if not root.left and not root.right: # If this is a leaf node 
            if n == sum: return True
            else: return False
        return self.gen(root.left, n, sum) or self.gen(root.right, n, sum)
